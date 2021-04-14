from setuptools import *

kwargs = {
    "author" : "Nathalon",
    "description" : "statix 1.0.0 [File Statistics Script]",
    "entry_points" : {"console_scripts" : ["statix=statix.statix:main"]},
    "license" : "GPL v3",
    "name" : "statix",
    "packages" : ["statix"],
    "version" : "V1.0.0",
}

setup(**kwargs)
