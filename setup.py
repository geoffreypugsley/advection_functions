from setuptools import setup

setup(
    name="advection_functions",
    author="Geoffrey Pugsley",
    author_email="gjp23@imperial.ac.uk",
    description="Python functions for satellite and meteorological data",
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
        "trackerlib",
    ],
    package_dir={"advection_functions": "advection_functions"},
    packages=["advection_functions"],
    package_data={"advection_functions": ["data/*", "config/*"]}
)
