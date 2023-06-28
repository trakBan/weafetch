# weafetch
### See the weather in terminal, neofetch style! ☁️🌡️

![final_weafetch](https://github.com/trakBan/weafetch/assets/81049050/e1b4d9d2-dedb-4e6d-9bcd-42eb833f4974)

## Usage
```
usage: wetfetch [-h] [-c CITY] [-d]

See the weather in terminal, neofetch style

options:
  -h, --help            show this help message and exit
  -c CITY, --city CITY  get a weather report for a different city
  -d, --debug           Get a more verbose error output
```

# Installation

```bash
git clone https://github.com/trakBan/weafetch.git
cd weafetch

# root is required
sudo pip install . || sudo pip install . --break-system-packages
```

## One line
```git clone https://github.com/trakBan/weafetch.git && cd weafetch && sudo pip install . || sudo pip install . --break-system-packages```


## JSON configuration

config file can be found at ```~/.config/weafetch/config.json```

```json
{
    "config": {
        "mph": false, # when false, displays wind in km/h, when true, mph
        "fahrenheit": false, # when false displays temperature in celsius, when true, in fahrenheit
        "common_space": 3 # how much space should be beetween art and desctiptions
    },
    "formatting": {
        "format": "%d%t%p%w", # order in which information is shown
        "values": {
            "d": "{desc}", # how desctiption should be shown
            "t": "{feel_like_temp}({real_temp}){unit_temp}", # how temperature should be shown
            "p": "{precip_chance}% | {precip}mm", # how precip (rain, snow) should be shown
            "w": "{wind_direction} {wind_speed}{unit_wind}" # how wind should be shown
        }
    }
}
```

### Keywords
```yaml
{desc} - description of weather, eg. "Light drizzle"
{feel_like_temp} - temperature that is perceived by humans , eg. 32
{real_temp} - actual temperature, eg, 30
{unit_temp} - shows symbol for celsius or fahrenheit, eg. °C
{precip_chance} - chance of rain, snow falling, eg 54%
{precip} - how much rain, snow is falling, eg 8mm
{wind_direction} - in which direction wind is blowing, eg. ↘
{wind_speed} - how fast wind is blowing eg. 4 units
{unit_wind} - shows measuring unit for wind, eg km/h, mph
```

weafetch is made possible by wttr.in api made by Igor Chubin
