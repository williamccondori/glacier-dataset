import os
import time
import rasterio
import numpy as np


# Libreria usada para realizar la segmentación de la imagen.
from sklearn import cluster

# Libreria para mostrar gráficos.
import matplotlib.pyplot as plt


def segment_with_kmeans(image_path, n_clusters, output_path, show_hists=False):
    """
    Realiza la segmentacion de la imagen con K-Means.
    :param image_path: Ruta de la imagen.
    :param n_clusters: Número de clústers.
    :param output_path: Ruta de salida de la imagen segmentada.
    :param show_hists: Indica si se muestran las distribuciones de histograma de la imagen segmentada.
    """

    start = time.time()

    print("Image segmentation... {image_path}".format(image_path=image_path))

    # Abrimos la imagen con rasterio.
    with rasterio.open(image_path, driver='GTiff') as dataset:
        print('[0] Image profile: {profile}'.format(profile=dataset.profile))
        band = dataset.read().astype(rasterio.float32)
    print('Image shape: {shape}'.format(shape=band.shape))

    # Redimensionamos la imagen a un vector de numpy.
    x = band.reshape((-1, 1))
    x = np.nan_to_num(x)  # Reemplaza los valores NaN por el valor 0.

    print('Vector shape: {shape}'.format(shape=x.shape))

    # Ejeutamos el algorítmo K.MEANS, el metodo fit() entrena el modelo.
    print('K-Means clusterization...')
    result = cluster.KMeans(n_clusters=n_clusters).fit(x)

    # Creamos un vector de numpy, donde cada valor es el cluster al que pertenece.
    print(result)
    x_clustered = result.labels_

    # Redimensionamos el vector a la forma de la imagen original.
    x_clustered = x_clustered.reshape(band.shape)
    print('Clustered shape: {shape}'.format(shape=x_clustered.shape))

    # Mostramos un grafico con el histograma de los valores de los clusters.
    if show_hists:
        plt.hist(x_clustered.flatten(), bins=n_clusters)
        plt.show()

    # if (n_clusters > 2):
    #    x_clustered = np.where(x_clustered == 1, 1, 0)

    # Finalmente, almacenamos el resultado en una imagen.
    profile = dataset.meta
    profile.update(driver='GTiff')
    profile.update(dtype=rasterio.float32)
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(x_clustered.astype(rasterio.float32))

    print('Image saved: {output_image_path}'.format(
        output_image_path=output_path))

    end = time.time()

    print('Segmentation time: {time}'.format(time=end - start))


# IMAGE_ID = 'IS002'  # Identificador de la imagen.
# IMAGE_NAME = 'IS002_NDSI'  # Nombre de la imagen.
# OUTPUT_IMAGE_PATH = 'segmented.tif'  # Ruta de la imagen segmentada.

# Se constuye la ruta de la imagen.
# IMAGE_FOLDER_PATH = os.path.join(BASE_PATH, IMAGE_ID)
# IMAGE_PATH = os.path.join(IMAGE_FOLDER_PATH, '{}.tif'.format(IMAGE_NAME))


BASE_PATH = 'D:\\Tesis\\Imágenes satelitales'
IMAGE_ID = 'IS004'
# 2 clústers
segment_with_kmeans(BASE_PATH + '\\'+IMAGE_ID+'\\'+IMAGE_ID +
                    '_NDSI.tif',  2, IMAGE_ID+'_NDSI-kms-2.tif')
segment_with_kmeans(BASE_PATH + '\\'+IMAGE_ID+'\\'+IMAGE_ID +
                    '_MNDSI.tif',   2, IMAGE_ID+'_MNDSI-kms-2.tif')
# 3 clústers
segment_with_kmeans(BASE_PATH + '\\'+IMAGE_ID+'\\'+IMAGE_ID +
                    '_NDSI.tif', 3, IMAGE_ID+'_NDSI-kms-3.tif')
segment_with_kmeans(BASE_PATH + '\\'+IMAGE_ID+'\\'+IMAGE_ID +
                    '_MNDSI.tif',  3, IMAGE_ID+'_MNDSI-kms-3.tif')
# 4 clústers
segment_with_kmeans(BASE_PATH + '\\'+IMAGE_ID+'\\'+IMAGE_ID +
                    '_NDSI.tif',  4, IMAGE_ID+'_NDSI-kms-4.tif')
segment_with_kmeans(BASE_PATH + '\\'+IMAGE_ID+'\\'+IMAGE_ID +
                    '_MNDSI.tif',  4, IMAGE_ID+'_MNDSI-kms-4.tif')
