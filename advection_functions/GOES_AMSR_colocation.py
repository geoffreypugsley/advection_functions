'''

A function to colocate GOES data with AMSR data.

Inputs: Lat, Lon, Time grid of GOES data, in general this will be a subset of the GOES CONUS granule. This data is typicaaly on a 10km grid for my research

Lat: (n x m) array of latitudes
Lon: (n x m) array of longitudes
Time: Scalar time value in UTC since we assume all the data is collected at the same time for the GOES geostationary data

Outputs: Colocated AMSR data on the same grid

Algorithm

- Check if AMSR data exists at the same time as the GOES data
- Check if the Lat Lon falls within the GOES bounding box
- For each GOES pixel check if an AMSR pixel exists within 1 degree
- If it does, calculate the distance to each of the pixels within the 1 degree
- Pick out the one with the smallest distance
- Read the AMSR data at that pixel

'''


import numpy as np
import h5py
from scipy.spatial import cKDTree  # For fast nearest neighbour search



def AMSR_colocated(gLon,gLat,gTime,AMSR_filename,AMSR_fieldname={'ChiSquared','ErrorLWP','ErrorTPW','ErrorWind','LandPercentage','LiquidWaterPath','QualityFlag','ReynoldsSST','SunGlintAngle','TimeHR','TotalPrecipitableWater','WindSpeed'}):
    '''
    Function to colocate AMSR data with GOES data#

    Inputs:

    gLon: 2D array of GOES longitudes
    gLat: 2D array of GOES latitudes
    gTime: scalar time value in UTC
    AMSR_filename: string of the AMSR filename, relevant data to be extracted, this is calculated in the calculate_AMSR_metadata function within advection funcs
    AMSR_fieldname: string of the fieldname in the AMSR data that we want to extract
    Outputs:

    AMSR_data: 2D array of the AMSR data colocated with the GOES data on the same grid as the GOES data

    '''

    year = gTime.year
    month = gTime.month

    data_path = f'/home/gjp23/projects/tests/multiple_trajectories/AMSR/AMSR_data/{year}/{month:02d}/{AMSR_filename}'
    
    
    # Read in the AMSR data

    # Open the HDF5 file
    with h5py.File(data_path, 'r') as f:
    # Access the subgroup named "SWATHS" within the "HDFEOS" group
        AMSR_lat = f['HDFEOS']['SWATHS']['AMSR2_Level2_Ocean_Suite']['Geolocation Fields']['Latitude'][:]
        AMSR_lon = f['HDFEOS']['SWATHS']['AMSR2_Level2_Ocean_Suite']['Geolocation Fields']['Longitude'][:]
        AMSR_time = f['HDFEOS']['SWATHS']['AMSR2_Level2_Ocean_Suite']['Geolocation Fields']['Time'][:]
        AMSR_data = f['HDFEOS']['SWATHS']['AMSR2_Level2_Ocean_Suite']['Data Fields']['AMSR_fieldname'][:]

    ### Just consider the data that is in the same latitude band as the GOES CONUS data, so that we remove all instances when the satellite is close to the poles/ not overhead the region of interest

    lats = AMSR_lat[(AMSR_lat > 14)&(AMSR_lat<54)]
    lons = AMSR_lon[(AMSR_lat > 14)&(AMSR_lat<54)]
    data = AMSR_data[(AMSR_lat > 14)&(AMSR_lat<54)]
    #times = AMSR_time[(AMSR_lat > 14)&(AMSR_lat<54)] ignore time for the time being as we can assume that the overpass occurs instantaneously; overpass takes place on the scale of minutes


    tree = cKDTree(np.concatenate((lons[:, None], lats[:, None]), axis=1))

    distances, indices =tree.query(np.concatenate((gLon.flatten()[:, None], gLat.flatten()[:, None]), axis=1)) # Find the nearest neighbour in the AMSR data to each of the GOES pixels, this has the same 

    data_colocated = data[indices]

    return 
