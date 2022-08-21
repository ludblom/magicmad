# -*- coding: utf-8 -*-


"""magicmad.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('magicmad/magicmad.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "magicmad",
    packages = ["magicmad"],
    entry_points = {
        "console_scripts": ['magicmad = magicmad.magicmad:main']
        },
    version = version,
    description = "A program to maintain your Magic The Gathering collection.",
    long_description = long_descr,
    author = "Ludvig Blomkvist",
    url = "https://github.com/ludblom/magicmad/",
    )
