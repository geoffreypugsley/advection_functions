#! /usr/bin/env python3

from setuptools import setup
import re

# Version code from https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
# VERSIONFILE = "csat2/_version.py"
# verstrline = open(VERSIONFILE, "rt").read()
# VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
# mo = re.search(VSRE, verstrline, re.M)
# if mo:
#     verstr = mo.group(1)
# else:
#     raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(
    name="advection_funcs",
    # version=verstr,
    author="Geoffrey Pugsley",
    author_email="gjp23@imperial.ac.uk",
    maintainer="Geoffrey Pugsley",
    maintainer_email="gjp23@imperial.ac.uk",
    description="Python functions for satellite and meteorological data ",
    url='https://github.com/geoffreypugsley/advection_functions',
    license="Not currently open source",
    install_requires=[
        "xarray",
        "numpy",
        "scipy",
        "netCDF4",
        "matplotlib",
        "scikit-learn",
        "google-cloud-storage",
        "pyyaml",
        "pyhdf",
    ],
    packages=["advection_functions"],
    # package_dir={"csat2": "csat2"},
    # package_data={"csat2": ["data/*", "config/*"]},
)
