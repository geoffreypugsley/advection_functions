from setuptools import setup

setup(
    name="advection_funcs",
    version="0.1.0",  # Update with your desired version number
    author="Geoffrey Pugsley",
    author_email="gjp23@imperial.ac.uk",
    description="Python functions for satellite and meteorological data",
    url='https://github.com/geoffreypugsley/advection_functions',
    license="Not currently open source",
    packages=["advection_functions"],
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
)