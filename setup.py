from setuptools import setup
#from os import mkdir, path
#from shutil import copy

"""
mkdirError = "You have to create ~./config/weafetch/ folder yourself"
copyError = (
    "You have to mannualy copy src/config.json to ~/.config/weafetch/"
)

path = f"{path.expanduser('~')}/.config/weafetch"

try:
    mkdir(path)

except FileExistsError:
    raise SystemExit("The folder ~/.config/weafetch already exists")

except Exception as e:
    raise SystemError(e, mkdirError)

try: copy("src/config.json", path)
except Exception as e: raise SystemExit(copyError, e)

with open("README.md", "r") as f:
    desc = f.read()
"""

setup(
    author="trakBan",
    description="See the weather in terminal, neofetch style",
    long_description=desc,
    name="weafetch",
    version="0.01a",
    install_requires=["requests", "argparse"],
    scripts=["weafetch", "src/artascii.py"],
)
