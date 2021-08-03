import rasterio
import matplotlib.pyplot as plt


ndsi_image = 'D:\\IMAGENES SATELITALES\\INAIGEM\\S2A_MSIL1C_20160529T152642_N0202_R025_T17LRL_20160529T153426.SAFE\\GRANULE\\L1C_T17LRL_A004884_20160529T153426\\IMG_DATA\\T17LRL_20160529T152642_B03.jp2'
ndsi_band = None


ndwi_image = 'C:\\Users\\William\\projects\\glacier-dataset\\T17LRL_20160529T152642_B11_upscaled.jp2'
ndwi_band = None

with rasterio.open(ndsi_image, driver='JP2OpenJPEG') as dataset_ndsi:
    print(dataset_ndsi.profile)
    ndsi_band = dataset_ndsi.read().astype(rasterio.float32)


with rasterio.open(ndwi_image, driver='JP2OpenJPEG') as dataset_ndwi:
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
with rasterio.open('mndwi.tif', 'w', **profile) as tiff:
    tiff.write(mndwi.astype(rasterio.float32))
