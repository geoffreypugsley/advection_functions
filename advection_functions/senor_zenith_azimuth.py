from haversine import haversine, Unit
import numpy as np

# Last checked 09/05/2024
# Data taken from https://www.noaasis.noaa.gov/GOES/goes_overview.html#:~:text=GOES%20East%20at%2075.2%C2%B0,GOES%20East%20or%20GOES%20West.

GOES = {
    'sub_lon': -137.2, # degrees,
    'sub_lat': 0, # degrees
    'alt' : 35786 # km
} 

def senor_azimuth_angle(lon, lat):
    '''Function to calculate the solar zenith angle for GOES West (G17) satellite data.
    Inputs: lon, lat (ndarray) - longitude and latitude of the satellite

    Ouputs: zenith_angle (ndarray) - solar zenith angle in degrees

    '''

    delta_lon = GOES['sub_lon'] - lon
    delta_lat = GOES['sub_lat'] - lat

    azimuth = np.arctan(delta_lon/delta_lat)
    return azimuth

def senor_zenith_angle(lon, lat):
    '''Function to calculate the solar zenith angle for GOES West (G17) satellite data.
    Inputs: lon, lat (ndarray) - longitude and latitude of the satellite

    Ouputs: zenith_angle (ndarray) - solar zenith angle in degrees

    '''

    delta_lon = GOES['sub_lon'] - lon
    delta_lat = GOES['sub_lat'] - lat

    delta_x = delta_lon * 111.1 ## convert to km
    delta_y = delta_lat * 111.1

    zenith_angle = np.arctan(np.sqrt(delta_x**2 + delta_y**2)/GOES['alt'])
    return zenith_angle
    
