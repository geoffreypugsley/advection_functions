import h5py
import numpy as np
import datetime
import os
import pandas as pd


def subset_around_point(matrix, initial_point, subset_size):
    """
    Extracts a subset of a matrix around the specified initial point.

    Parameters:
    - matrix: The input matrix.
    - initial_point: Tuple containing (row, column) indices of the initial point.
    - subset_size: Size of the subset to be extracted.

    Returns:
    - subset_matrix: The extracted subset.
    """

    # Calculate the indices for the subset
    start_row = max(0, initial_point[1] - subset_size // 2)
    end_row = min(matrix.shape[0], start_row + subset_size)

    start_col = max(0, initial_point[0] - subset_size // 2)
    end_col = min(matrix.shape[1], start_col + subset_size)

    # Extract the subset
    subset_matrix = matrix[start_row:end_row, start_col:end_col]

    return subset_matrix


def get_min_max(dataset, field):
    min_val = np.min(dataset[field][:])
    max_val = np.max(dataset[field][:])
    return min_val, max_val

def adjust_longitudes(longitudes):
    # Add 360 to any negative longitudes
    return np.where(longitudes < 0, longitudes + 360, longitudes)



def get_min_max_lat_lon_time(file_path):
    with h5py.File(file_path, 'r') as f:
        # Access the Geolocation Fields dataset
        geo_fields = f['HDFEOS']['SWATHS']['AMSR2_Level2_Ocean_Suite']['Geolocation Fields']
        
        # Extract latitude data
        latitudes = geo_fields['Latitude'][:]
        
        # Create a mask for latitude
        lat_mask = (latitudes > 30) & (latitudes < 60)
        
        # Extract longitude data based on latitude mask
        longitudes = geo_fields['Longitude'][lat_mask]
        
        # Adjust longitudes to be within the range of 0 to 360 degrees
        adjusted_longitudes = adjust_longitudes(longitudes)
        
        # Get min and max latitude
        min_lat, max_lat = np.min(latitudes[lat_mask]), np.max(latitudes[lat_mask])
        
        # Get min and max longitude after adjustment
        min_lon, max_lon = np.min(adjusted_longitudes), np.max(adjusted_longitudes)
        
        # Get min and max time
        min_time, max_time = get_min_max(geo_fields, 'Time')
        
        return min_lat, max_lat, min_lon, max_lon, min_time, max_time



    

def calculate_AMSR_metadata(year,month):
    '''
    Function to calculate the metadata for the AMSR data

    Returns a dataframe with the metadata for the AMSR data
    '''
    data_directory = f'/home/gjp23/projects/tests/multiple_trajectories/AMSR/AMSR_data/{year}/{month}'


    start_date = datetime.datetime(1993, 1, 1, 0, 0, 0) # reference date for which the AMSR time is measure from

    #working_directory = os.getcwd()



    # Create an empty list to store the data
    data = []

    # Loop through each .he5 file in the directory
    for filename in os.listdir(data_directory):
        if filename.endswith(".he5"):
            file_path = os.path.join(data_directory, filename)
            min_lat, max_lat, min_lon, max_lon, min_time_seconds, max_time_seconds = get_min_max_lat_lon_time(file_path)

            min_time = start_date + datetime.timedelta(seconds=min_time_seconds)
            max_time = start_date + datetime.timedelta(seconds=max_time_seconds)
            
            # Append data to the list
            data.append([filename, min_lat, max_lat, min_lon, max_lon, min_time, max_time])

    # Create a pandas DataFrame
    df = pd.DataFrame(data, columns=['Filename', 'Min_Latitude', 'Max_Latitude', 'Min_Longitude', 'Max_Longitude', 'Min_Time', 'Max_Time'])

    return df
        

