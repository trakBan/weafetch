from json import loads
from requests import get
from itertools import zip_longest


city: str = "Novska"
url: str = f"http://wttr.in/{city}?format=j1"

error_internet: str = "There was a problem while fetching the data, error code:"
common_space = 3


init = get(url)
getip = get("https://ipinfo.io/json")


if init.status_code != 200 or getip.status_code != 200:
    raise Exception(error_internet)

city: str = loads(getip.text)["city"]
weatherRaw: dict = loads(init.text)


WHITE, END = "", ""
neutral = f"""{WHITE}    .--.  {END}
{WHITE} .-(    ).{END}
{WHITE}(___.__)__){END}"""


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
        f'{weather["feels_like"]}({weather["temp"]})C',
        f'{weather["rain_chance"]}% | {weather["rain_levels"]}mm',
        f'{weather["wind_speed"]}km/h | {wind}',
    ]


def main() -> None:

    longest: int = max([len(x) for x in neutral.splitlines()])
    for art, desc in zip_longest(neutral.splitlines(), descriptors, fillvalue=""):

        print(art, " " * (longest - len(art)), end=" " * common_space)

        print(desc)


if __name__ == "__main__":
    getWeather()
    main()
