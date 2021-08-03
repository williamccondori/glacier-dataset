import rasterio
import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt

image = 'mndwi.tif'

with rasterio.open(image, driver='GTiff') as dataset:
    print(dataset.profile)
    band = dataset.read().astype(rasterio.float32)

image = np.where(band < 0.4, -1, band)

x = image.reshape((-1, 1))
x = np.nan_to_num(x)

result = cluster.KMeans(n_clusters=4).fit(x)

x_clustered = result.labels_
x_clustered = x_clustered.reshape(image.shape)
x_clustered = np.where((x_clustered == 1), x_clustered, -1)

plt.hist(x_clustered.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.show()

# save ndwi image
profile = dataset.meta
profile.update(driver='GTiff')
profile.update(dtype=rasterio.float32)
with rasterio.open('k-means-mndwi-4.tif', 'w', **profile) as tiff:
    tiff.write(x_clustered.astype(rasterio.float32))
