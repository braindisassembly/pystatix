from setuptools import *

kwargs = {
    "author" : "BrainDisassembly",
    "author_email" : "braindisassm@gmail.com",
    "description" : "PyStatix 1.0.0 [File Statistics Script]",
    "entry_points" : {"console_scripts" : ["pystatix=pystatix.pystatix:main"]},
    "license" : "GPL v3",
    "name" : "pystatix",
    "packages" : ["pystatix"],
    "version" : "V1.0.0",
}

setup(**kwargs)
