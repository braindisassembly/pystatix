from setuptools import *

kwargs = {
    "author" : "BrainDisassembly",
    "author_email" : "braindisassm@gmail.com",
    "description" : "Statix 1.0.0 [File Statistics Script]",
    "entry_points" : {"console_scripts" : ["Statix=Statix.Statix:main"]},
    "license" : "GPL v3",
    "name" : "Statix",
    "packages" : ["Statix"],
    "version" : "V1.0.0",
}

setup(**kwargs)
