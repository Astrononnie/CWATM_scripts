# -------------------------------------------------------------------------
#
#     #######    ########   ####     ####  
#    ##     ##      ##     ##   ##  ##   ##
#    ##             ##     ###      ###    
#    ##             ##       ###      ###  
#    ##     ####    ##         ###      ###
#    ##     ##      ##     ##   ##  ##   ##
#     #######    ########   #####    ##### 
#
# Name:        change_prec_CWATM
# Purpose:     Change the Precipitation value to study the effects of precipitation
#              on the surrounding area in the Rhine River. The code can be 
#              changed to suite other modifications to the netCDF4 files.  
#
# Author:      M. Puma; N. Woodruff

# Created:     16/07/2019
# -------------------------------------------------------------------------
from netCDF4 import Dataset
import numpy as np

# The netCDF4 file in the same folder as this python script
path = "pr_rhine_original.nc"

with Dataset(path) as data:
    
    lon = data["lon"][:]
    lat = data["lat"][:]
    time = data["time"][:]
    prec = data["prec"][:,:,:]
    print(data)
    
# the new file is saved in the same folder
path2 = "pr_rhine.nc"
data2 = Dataset(path2, 'w', format='NETCDF4_CLASSIC')

# Create Dimensions
lonDim = data2.createDimension('lon',14)
latDim = data2.createDimension('lat',12)
timeDim = data2.createDimension('time',19358)

# Create Variables
lonVar = data2.createVariable('lon', np.float32, dimensions = ("lon"))
latVar = data2.createVariable('lat', np.float32, dimensions = ("lat"))
timeVar = data2.createVariable('time', np.float32, dimensions = ("time"))
precVar = data2.createVariable('prec', np.float32, dimensions = ("time","lat","lon"))

# Define pr_rhine variables to be copies from the pr_rhine_original variables
lonVar[:] = lon[:]
latVar[:] = lat[:]
timeVar[:] = time[:]

# The meat of this program. Changing the precipitation before saving it to the .nc file
precVar[:,:,:] = 1.2*prec[:,:,:]

data2.close()
