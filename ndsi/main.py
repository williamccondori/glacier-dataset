import rasterio
import matplotlib.pyplot as plt

"""
El indice NDSI para Sentinel-2 es:
NDSI (Sentinel 2) = (B3 – B11) / (B3 + B11)
"""

green_image = 'D:\\IMAGENES SATELITALES\\INAIGEM\\S2A_MSIL1C_20160529T152642_N0202_R025_T17LRL_20160529T153426.SAFE\\GRANULE\\L1C_T17LRL_A004884_20160529T153426\\IMG_DATA\\T17LRL_20160529T152642_B03.jp2'
green_band = None


swir_image = 'C:\\Users\\William\\projects\\glacier-dataset\\T17LRL_20160529T152642_B11_upscaled.jp2'
swir_band = None

with rasterio.open(green_image, driver='JP2OpenJPEG') as dataset_green:
    print(dataset_green.profile)
    green_band = dataset_green.read().astype(rasterio.float32)


with rasterio.open(swir_image, driver='JP2OpenJPEG') as dataset_swir:
    print(dataset_swir.profile)
    swir_band = dataset_swir.read().astype(rasterio.float32)

# calculate ndsi
ndsi = (green_band - swir_band) / (green_band + swir_band)

# show histogram
plt.hist(ndsi.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.show()

print(ndsi.shape)

# save ndsi image
profile = dataset_green.meta
profile.update(driver='GTiff')
profile.update(dtype=rasterio.float32)
with rasterio.open('ndsi.tif', 'w', **profile) as tiff:
    tiff.write(ndsi.astype(rasterio.float32))
