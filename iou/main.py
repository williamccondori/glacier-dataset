import rasterio
import numpy as np


def evaluate(image, folder):
    with rasterio.open(f'{folder}\\mask.tif', driver='GTiff') as dataset_original:
        # print(dataset_original.profile)
        band_original = dataset_original.read(1)
    image_original = np.array(band_original, dtype=bool)
    # print(image_original.shape)
    # print(image_original)

    with rasterio.open(f'{folder}\\{image}.tif', driver='GTiff') as dataset_2:
        # print(dataset_2.profile)
        band_2 = dataset_2.read(1)
    image_2 = np.array(band_2, dtype=bool)
    # print(image_2.shape)
    # print(image_2)

    overlap = image_original * image_2  # Logical AND
    union = image_original + image_2  # Logical OR

    IOU = overlap.sum()/float(union.sum())

    print(f'{image} IOU: {IOU}')


folder = 'S2A_MSIL1C_20160529T152642_N0202_R025_T17LRL_20160529T153426'
print(folder)
evaluate('t-ndsi', folder)
evaluate('t-mndsi', folder)
evaluate('k-means-ndsi-2', folder)
evaluate('k-means-ndsi-3', folder)
evaluate('k-means-ndsi-4', folder)
evaluate('k-means-mndsi-2', folder)
evaluate('k-means-mndsi-3', folder)
evaluate('k-means-mndsi-4', folder)

folder = 'S2A_MSIL1C_20160618T152642_N0204_R025_T17LRL_20160618T153021'
print(folder)
evaluate('t-ndsi', folder)
evaluate('t-mndsi', folder)
evaluate('k-means-ndsi-2', folder)
evaluate('k-means-ndsi-3', folder)
evaluate('k-means-ndsi-4', folder)
evaluate('k-means-mndsi-2', folder)
evaluate('k-means-mndsi-3', folder)
evaluate('k-means-mndsi-4', folder)
