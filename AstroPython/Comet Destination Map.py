import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from astropy.coordinates import SkyCoord
from datetime import datetime
import astropy.units as u
import cartopy.crs as ccrs
import matplotlib.dates as mdates

data = pd.read_csv("/workspaces/blank-app/AstroPython/Data/HaleBopp_1985_2005_ts10d.csv")
data2 = pd.read_csv("/workspaces/blank-app/AstroPython/Data/hygdata_v3.csv")
data2 = data2[data2['mag'] < 4]

ra1 = data[' RA (J2000)'].tolist()
dec1 = data[' Dec (J2000)'].tolist()
dates = pd.to_datetime(data['Date and Time'], format='%Y-%m-%d %H:%M:%S')

ra2 = data2['ra'].tolist()
dec2 = data2['dec'].tolist()

# Convert RA and DEC from string to SkyCoord objects
coords = SkyCoord(ra=ra1, dec=dec1, unit=(u.hourangle, u.deg))
coords2 = SkyCoord(ra=ra2, dec=dec2, unit=(u.hourangle, u.deg))

# Extract RA and DEC in degrees for spherical plotting
ra_deg = coords.ra.deg
dec_deg = coords.dec.deg

ra_deg2 = coords2.ra.deg
dec_deg2 = coords2.dec.deg
star_magnitudes = data2['mag']

# Convert RA to radians and shift range for Mollweide (-π to π)
ra_rad = np.deg2rad(ra_deg)
ra_rad = np.remainder(ra_rad + np.pi, 2 * np.pi) - np.pi  # Shift RA to (-π, π)

# Convert RA to radians and shift range for Mollweide (-π to π)
ra_rad2 = np.deg2rad(ra_deg2)
ra_rad2 = np.remainder(ra_rad2 + np.pi, 2 * np.pi) - np.pi  # Shift RA to (-π, π)

# Convert DEC to radians
dec_rad = np.deg2rad(dec_deg)

# Convert DEC to radians
dec_rad2 = np.deg2rad(dec_deg2)

# Plot on Mollweide projection
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='mollweide')

sizes = 30 * (1 - (star_magnitudes - star_magnitudes.min()) /
                    (star_magnitudes.max() - star_magnitudes.min()))

#ax.scatter(ra_rad, dec_rad, marker='o', s=3, color='blue')
ax.scatter(ra_rad2, dec_rad2, marker='o', s=sizes, color='k')

sc = ax.scatter(
    ra_rad, dec_rad, s=8, c=dates, cmap='viridis')

cbar = plt.colorbar(sc,  fraction=0.02)
cbar.set_label('Years', fontsize=12)
cbar.ax.set_yticklabels(pd.to_datetime(cbar.get_ticks()).strftime(date_format='%Y'))

# Customize the plot
ax.set_xlabel('Right Ascension (hours)', fontsize=12)
ax.set_ylabel(r'Declination ($^\circ$)', fontsize=12)
#ax.set_title('C/1995 O1 (Hale-Bopp)', fontsize=18, pad=20)

# Grid and labels
ax.grid(True)
plt.show()