from setuptools import setup, find_packages
import os
from shutil import copy


mkdirError = "You have to create ~./config/weafetch/ folder yourself"
copyError = "You have to mannualy copy src/config.json to ~/.config/weafetch/"
sudoUserError = "There has been a problem with fetching your username, USERNAME/.local/weafetch enter it mannualy: "

try: user: str = os.environ.get("SUDO_USER")
except: user: str = input(sudoUserError)
path: str = f"/home/{user}/.config/weafetch"

if os.path.isfile(path + "/config.json") == False:
    try: os.mkdir(path)
    except Exception as e: raise SystemError(e, mkdirError)

    try: copy("src/config.json", path)
    except Exception as e: raise SystemExit(copyError, e)


with open("README.md", "r") as f:
    desc = f.read()


setup(
    author="trakBan",
    description="See the weather in terminal, neofetch style",
    long_description=desc,
    name="weafetch",
    version="0.03a",
    packages=find_packages(),
    install_requires=["requests", "argparse"],
    scripts=["weafetch"],
)
