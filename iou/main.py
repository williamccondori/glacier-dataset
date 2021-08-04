import numpy as np
import rasterio

with rasterio.open('S2A_MSIL1C_20160529T152642_N0202_R025_T17LRL_20160529T153426\\mask.tif', driver='GTiff') as dataset_original:
    print(dataset_original.profile)
    band_original = dataset_original.read(1)
image_original = np.array(band_original, dtype=bool)
print(image_original.shape)
print(image_original.dtype)

with rasterio.open('S2A_MSIL1C_20160529T152642_N0202_R025_T17LRL_20160529T153426\\mndsi.tif', driver='GTiff') as dataset_2:
    print(dataset_2.profile)
    band_2 = dataset_2.read(1)
image_2 = np.array(band_2, dtype=bool)
print(image_2.shape)
print(image_2.dtype)


overlap = image_original * image_2  # Logical AND
union = image_original + image_2  # Logical OR

IOU = overlap.sum()/float(union.sum())

print(IOU)
