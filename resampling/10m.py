import os
import rasterio
from rasterio.enums import Resampling

upscale_factor = 2


with rasterio.open('2018_reprojected.tif', driver='GTiff') as dataset:

    print(dataset.meta)

    # resample data to target shape
    data = dataset.read(
        out_shape=(
            dataset.count,
            int(7790),
            int(17885)
        ),
        resampling=Resampling.bilinear
    )

    # scale image transform
    transform = dataset.transform * dataset.transform.scale(
        (7790 / data.shape[-1]),
        (17885 / data.shape[-2])
    )

    print(transform)

    # write data to new file
    with rasterio.open('2018_reprojected_upscaled.tif', 'w', driver='GTiff',
                       width=data.shape[-1], height=data.shape[-2], count=data.shape[0],
                       crs=dataset.crs, transform=transform, dtype=data.dtype) as out:
        out.write(data)
