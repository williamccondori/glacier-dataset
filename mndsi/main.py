import rasterio
import matplotlib.pyplot as plt


ndsi_image = 'ndsi.tif'
ndsi_band = None


ndwi_image = 'ndwi.tif'
ndwi_band = None

with rasterio.open(ndsi_image, driver='GTiff') as dataset_ndsi:
    print(dataset_ndsi.profile)
    ndsi_band = dataset_ndsi.read().astype(rasterio.float32)


with rasterio.open(ndwi_image, driver='GTiff') as dataset_ndwi:
    print(dataset_ndwi.profile)
    ndwi_band = dataset_ndwi.read().astype(rasterio.float32)

mndwi = ndsi_band - ndwi_band

# show histogram
plt.hist(mndwi.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.show()

print(mndwi.shape)

# save ndsi image
profile = dataset_ndsi.meta
profile.update(driver='GTiff')
profile.update(dtype=rasterio.float32)
with rasterio.open('mndsi.tif', 'w', **profile) as tiff:
    tiff.write(mndwi.astype(rasterio.float32))
