import rasterio
import matplotlib.pyplot as plt

"""
El indice NDWI para Sentinel-2 es:
NDWI (Sentinel 2) = (B3 – B8) / (B3 + B8)
"""

green_image = 'D:\\IMAGENES SATELITALES\\INAIGEM\\S2A_MSIL1C_20160618T152642_N0204_R025_T17LRL_20160618T153021.SAFE\\GRANULE\\L1C_T17LRL_A005170_20160618T153021\\IMG_DATA\\T17LRL_20160618T152642_B03.jp2'
green_band = None


nir_image = 'D:\\IMAGENES SATELITALES\\INAIGEM\\S2A_MSIL1C_20160618T152642_N0204_R025_T17LRL_20160618T153021.SAFE\\GRANULE\\L1C_T17LRL_A005170_20160618T153021\\IMG_DATA\\T17LRL_20160618T152642_B08.jp2'
nir_band = None

with rasterio.open(green_image, driver='JP2OpenJPEG') as dataset_green:
    print(dataset_green.profile)
    green_band = dataset_green.read().astype(rasterio.float32)


with rasterio.open(nir_image, driver='JP2OpenJPEG') as dataset_nir:
    print(dataset_nir.profile)
    nir_band = dataset_nir.read().astype(rasterio.float32)

# calculate ndwi
ndwi = (green_band - nir_band) / (green_band + nir_band)

# show histogram
plt.hist(ndwi.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.show()

print(ndwi.shape)

# save ndwi image
profile = dataset_green.meta
profile.update(driver='GTiff')
profile.update(dtype=rasterio.float32)
with rasterio.open('ndwi.tif', 'w', **profile) as tiff:
    tiff.write(ndwi.astype(rasterio.float32))
