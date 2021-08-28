import rasterio
import numpy as np
import matplotlib.pyplot as plt


image = 'k-means-mndsi-4'

with rasterio.open(f'S2A_MSIL1C_20160618T152642_N0204_R025_T17LRL_20160618T153021\\{image}.tif', driver='GTiff') as dataset:
    print(dataset.profile)
    band = dataset.read().astype(rasterio.float32)

x_band = np.where((band == 1), 1, 0)

profile = dataset.meta
profile.update(driver='GTiff')
profile.update(dtype=rasterio.float32)
with rasterio.open(f'{image}.tif', 'w', **profile) as tiff:
    tiff.write(x_band.astype(rasterio.float32))
