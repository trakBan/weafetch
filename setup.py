from setuptools import setup
from os import environ, mkdir
from shutil import copy


mkdirError = "You have to create ~./config/weafetch/ folder yourself"
copyError = "You have to mannualy copy.json config and artascii.py to ~/.config/weafetch/"


path = f"{environ['HOME']}/.config/weafetch/"
print(path)

try: mkdir(path)
except Exception as e: raise SystemError(mkdirError)

try:
    copy("artascii.py", path)
    copy("config.json", path)

except Exception as e: raise SystemError(copyError)


with open("README.md", "r") as f:
    desc = f.read()


setup(

    author="trakBan",
    description="See the weather in terminal, neofetch style",
    long_description=desc,
    name="weafetch",
    version="0.01a",

    install_requires=[
        "requests",
        "argparse"
    ],
    scripts=[
        "weafetch"
    ]
)