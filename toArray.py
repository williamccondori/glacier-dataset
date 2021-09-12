import matplotlib.pyplot as plt
import numpy as np
import rasterio
from rasterio.plot import reshape_as_image

with rasterio.open('IS003.311.tif', 'r') as dataset:
    array = dataset.read()
    np.save('gray.npy', reshape_as_image(array))

with rasterio.open('prueba2.tif', 'r') as dataset:
    array = dataset.read()
    np.save('rgb.npy', reshape_as_image(array))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(30, 10))
img = np.load('rgb.npy')
img = img[:, :, 2]
print(img.shape)
mask = np.load('gray.npy')
print(mask.shape)
ax1.imshow(img)
ax2.imshow(mask)
ax3.imshow(img)
ax3.imshow(mask, alpha=0.4)
plt.axis("off")

plt.show()

print(np.amin(mask))
print(np.amax(mask))
