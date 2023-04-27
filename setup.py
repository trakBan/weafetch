from setuptools import setup


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