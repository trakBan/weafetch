from json import loads
from requests import get
from itertools import zip_longest


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


try: getip = get("https://ipinfo.io/json")
except Exception as e: raise SystemExit(error_internet)

city: str = loads(getip.text)["city"]
url: str = f"http://wttr.in/{city}?format=j1"

try: init = get(url)
except Exception as e: raise SystemExit(error_internet)

weatherRaw: dict = loads(init.text)


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
        "country": weatherRaw["nearest_area"][0]["country"][0]["value"]
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
        f'{weather["city"]}, {weather["country"]}',
        weather["desc"],
        f'{weather["feels_like"]}({weather["temp"]})°C',
        f'{weather["rain_chance"]}% | {weather["rain_levels"]} mm',
        f'{weather["wind_speed"]}km/h {wind}',
    ]


def getArt(art: str = "") -> str:

    desc = weather.get("desc", None).lower()

    if "cloud" in desc:
        art += cloud + "\n"
    if "rain" in desc:
        art += rain + "\n"
    else:
        art = neutral

    return art

def main() -> None:

    artFull: str = getArt()

    longest: int = max([len(x) for x in artFull.splitlines()])
    for art, desc in zip_longest(artFull.splitlines(), descriptors, fillvalue=""):

        print(art, " " * (longest - len(art)), end=" " * common_space)
        print(desc)


if __name__ == "__main__":
    getWeather()
    main()
    print()
