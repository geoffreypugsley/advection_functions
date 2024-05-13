from datetime import datetime, timedelta
import numpy as np
from advection_functions import advection_funcs

class AirParcel:
    def __init__(self, start_time, duration, t_step, init_lat, init_lon, spatial_resolution, spatial_extent, wind_data):
        self.start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")  # Start time of the simulation
        self.time = self.start_time                        # this will update by a single time step each time
        self.duration = duration                          # Duration of the simulation
        self.t_step = t_step                              # Time step of the simulation
        self.lat = init_lat                          # Initial latitude of the air parcel
        self.lon = init_lon                          # Initial longitude of the air parcel
        self.spatial_resolution = spatial_resolution      # Spatial resolution of the simulation
        self.spatial_extent = spatial_extent              # Spatial extent of the simulation
        self.wind_data = wind_data                        # Wind data for advection
    
    def get_wind(self):
        return self.winddata.get_data(self.lon, self.lat, self.time)
    
    def update_pos(self):
        wind = self.get_wind()
        dist_x = wind[0] * (self.time_step.total_seconds() / 1000.0) # distance travelled in x direction in local cartesian coordinates in km
        dist_y = wind[1] * (self.time_step.total_seconds() / 1000.0)
        nlon, nlat = advection_funcs.xy_offset_to_ll(self.current_position[0], self.current_position[1], dist_x, dist_y) # returns the new lon and lat
        
        # Apply the mask of the initial position to the updated position: this is not correct
        mask = self.current_position.mask
        self.current_position = np.ma.array([nlon, nlat], mask=mask)
        #print("Updated mask:", self.current_position.mask)  # Debugging
        
        self.current_time += self.time_step

    def advect_trajectory(self):
        current_time = self.start_time
        trajectories = []

        for _ in range(self.duration):
            # Example advecting method, you can replace this with your own logic
            # Here, we just move the air parcel by adding wind velocities
            u_wind = self.wind_data[current_time]['u_wind']
            v_wind = self.wind_data[current_time]['v_wind']

            new_lat = self.init_lat + u_wind * self.t_step
            new_lon = self.init_lon + v_wind * self.t_step

            trajectories.append((current_time, new_lat, new_lon))
            current_time += timedelta(hours=1)

        return trajectories

    def calculate_lwp(self, lat, lon):
        # Example calculation for LWP using dummy values
        lwp = 0.001 * lat + 0.002 * lon
        return lwp

    def calculate_cf(self, lat, lon):
        # Example calculation for CF using dummy values
        cf = 0.1 * lat + 0.05 * lon
        return cf

    def get_data(self, product):
        data = {}

        for parcel_time, parcel_lat, parcel_lon in self.advect_trajectory():
            if product == 'LWP':
                data[parcel_time] = self.calculate_lwp(parcel_lat, parcel_lon)
            elif product == 'CF':
                data[parcel_time] = self.calculate_cf(parcel_lat, parcel_lon)

        return data

# Example wind data
wind_data = {
    datetime(2024, 5, 10, 0, 0, 0): {'u_wind': 10, 'v_wind': 5},
    datetime(2024, 5, 10, 1, 0, 0): {'u_wind': 12, 'v_wind': 6},
    # Add more wind data for each hour...
}

# Example usage:
start_time = "2024-05-10 00:00:00"    # Start time of simulation
duration = 24                          # Duration of simulation in hours
t_step = 1                             # Time step of simulation in hours
init_lat = 40.7128                     # Initial latitude of air parcel (e.g., latitude of New York City)
init_lon = -74.0060                    # Initial longitude of air parcel (e.g., longitude of New York City)
spatial_resolution = "1 km"            # Spatial resolution of simulation
spatial_extent = "100x100 km"          # Spatial extent of simulation

parcel = AirParcel(start_time, duration, t_step, init_lat, init_lon, spatial_resolution, spatial_extent, wind_data)

# Get data for CF
cf_data = parcel.get_data('CF')
print("Cloud Fraction Data:")
for time, cf in cf_data.items():
    print(f"At {time}: CF = {cf}")

# Get data for LWP
lwp_data = parcel.get_data('LWP')
print("\nLiquid Water Path Data:")
for time, lwp in lwp_data.items():
    print(f"At {time}: LWP = {lwp}")





































