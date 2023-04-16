# Formatted using black
from itertools import zip_longest
import json
from datetime import datetime

from requests import get
import wetfetch_ascii as wfa
import argparse


def Weather(city: str) -> dict:
    geocodeUrl: str = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&language=en&count=1&format=json"
    geocode: dict = json.loads(get(geocodeUrl).text)["results"][0]

    latitude, longitude = geocode["latitude"], geocode["longitude"]

    weatherUrl: str = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,,apparent_temperature,windspeed_10m,winddirection_10m,relativehumidity_2m,rain,snowfall,cloudcover,is_day&daily=sunrise,sunset&forecast_days=1&timezone=auto"
    weather: dict = json.loads(get(weatherUrl).text)

    return weather


def Hour() -> int:
    return datetime.now().hour + (
        1 if (datetime.now().minute > 30 and datetime.now().hour != 23) else 0
    )


def formattedWeather() -> dict:
    weather: dict = Weather(city)
    hour: int = Hour()

    windAngle = weather["hourly"]["winddirection_10m"][hour]
    windDirection = ""
    windDirection = (
        "↑" if (windAngle in range(0, 45) or windAngle in range(315, 360))
        else windDirection
    )
    windDirection = ">" if (windAngle in range(45, 135)) else windDirection
    windDirection = "<" if (windAngle in range(225, 315)) else windDirection
    windDirection = "↓" if (windAngle in range(135, 225)) else windDirection

    formWeather: dict = {
        "Wind": [weather["hourly"]["windspeed_10m"][hour], "km/h", "|", windDirection],
        "Temperature": [
            round(weather["hourly"]["temperature_2m"][hour]),
            f'({round(weather["hourly"]["apparent_temperature"][hour])})',
            "°C",
        ],
        "Humidity": [weather["hourly"]["relativehumidity_2m"][hour], "%"],
        "Rain": [weather["hourly"]["rain"][hour], "mm"],
        "Clouds": [weather["hourly"]["cloudcover"][hour], "%"],
    }

    return formWeather


def getArt() -> str:
    weather = formattedWeather()

    comparableWeather = {}
    for x in weather.items():
        comparableWeather[x[0]] = x[1][0]

    if all([comparableWeather["Rain"] < 0.25, comparableWeather["Clouds"] < 25]):
        art = wfa.neutral
    elif all([comparableWeather["Rain"] > 0.25, comparableWeather["Clouds"] < 25]):
        art = wfa.rain
    elif all([comparableWeather["Rain"] > 0.25, comparableWeather["Clouds"] > 25]):
        art = wfa.cloud + wfa.rain
    else:
        art = wfa.neutral

    return art


def parseArgs():
    parser = argparse.ArgumentParser(
        prog="wetfetch",
        description="See the weather in terminal, neofetch style",
    )

    parser.add_argument(
        "-c", "--city", type=str, help="get a weather report for a different city"
    )

    return parser.parse_args()


def main():
    weather = formattedWeather()
    art = getArt()

    maxAscii = max([len(x) for x in art.splitlines()])
    for asc, (desc, value) in zip_longest(
        art.splitlines(), weather.items(), fillvalue=("", "")
    ):
        print(
            asc if type(asc) is not tuple else "  ",
            " " * (maxAscii - len(asc)),
            end="   ",
        )

        print(
            desc, " ".join([str(x) for x in value]),
            sep=(": ") if value != "" else ""
        )


if __name__ == "__main__":
    args = parseArgs()
    city = args.city

    main()
