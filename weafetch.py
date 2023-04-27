from json import loads
from itertools import zip_longest

from requests import get
import argparse


error_internet: str = "There seems to be a problem with internet."
common_space = 3


neutral = """   .--.
 .-(    ).
(___.__)__)"""

cloud = """  .-.
 (   ). 
(___(__)"""

rain = """  ‘ ‘ ‘ ‘
‘ ‘ ‘ ‘"""

fog = """ 
_ - _ - _ -
  _ - _ - _
 _ - _ - _ -"""

clear = """
  \   /
   .-.
― (   ) ―
   `-’
  /   \\"""

partly = """
   \  /
 _ /"".-.
   \_(   ).
   /(___(__)
"""


def getWeather():

    currentWeather: dict = weatherRaw["weather"][0]["hourly"][0]

    global weather
    weather = {
        "temp": currentWeather["tempC"],
        "feels_like": currentWeather["FeelsLikeC"],
        "rain_chance": currentWeather["chanceofrain"],
        "rain_levels": currentWeather["precipMM"],
        "desc": currentWeather["weatherDesc"][0]["value"],
        "wind_speed": currentWeather["windspeedKmph"],
        "wind_direction": currentWeather["winddir16Point"],
        "city": weatherRaw["nearest_area"][0]["areaName"][0]["value"],
        "country": weatherRaw["nearest_area"][0]["country"][0]["value"],
    }

    windDirection = weather["wind_direction"]
    wind = ""
    wind = "↑" if windDirection == "N" else wind
    wind = "→" if windDirection == "E" else wind
    wind = "←" if windDirection == "W" else wind
    wind = "↓" if windDirection == "S" else wind

    wind = "↖" if windDirection in ["WNW", "NW", "NNW"] else wind
    wind = "↗" if windDirection in ["NNE", "NE", "ENE"] else wind
    wind = "↙" if windDirection in ["WSW", "WS", "SSW"] else wind
    wind = "↘" if windDirection in ["SSE", "ES", "ESE"] else wind

    global descriptors
    descriptors = [
        weather["desc"],
        f'{weather["feels_like"]}({weather["temp"]})°C',
        f'{weather["rain_chance"]}% | {weather["rain_levels"]} mm',
        f'{wind} {weather["wind_speed"]}km/h',
    ]


def getArt(art: str = "") -> str:

    desc = weather.get("desc", None).lower()
    entered = False

    if "cloud" in desc:
        art += cloud + "\n"
        entered = True
    if "rain" in desc:
        art += rain + "\n"
        entered = True
    if "fog" in desc:
        art = fog
        entered = True
    if "clear" in desc:
        art = clear
        entered = True
    if "partly" in desc:
        art = partly
        entered = True

    if entered == False:
        art = neutral

    return art


def parseArgs():

    parser = argparse.ArgumentParser(
        prog="wetfetch",
        description="See the weather in terminal, neofetch style",
    )

    parser.add_argument(
        "-c", "--city", type=str, help="get a weather report for a different city"
    )

    parser.add_argument(
        "-d", "--debug", action="store_true", help="Get a more verbose error output"
    )

    return parser.parse_args()


def main() -> None:

    artFull: str = getArt()

    longest: int = max([len(x) for x in artFull.splitlines()])
    for art, desc in zip_longest(artFull.splitlines(), descriptors, fillvalue=""):

        print(art, " " * (longest - len(art)), end=" " * common_space)
        print(desc)


if __name__ == "__main__":

    args = parseArgs()
    city = args.city

    city = "" if city is None else city

    url: str = f"http://wttr.in/{city}?format=j1"
    try:
        init = get(url)
    except Exception as e:
        raise SystemExit(error_internet, e if args.debug else None)

    weatherRaw: dict = loads(init.text)

    getWeather()

    print(f'{weather["city"]}, {weather["country"]}\n')
    main()
    print()
