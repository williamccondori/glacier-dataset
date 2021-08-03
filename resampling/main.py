import os
import rasterio
from rasterio.enums import Resampling

upscale_factor = 2

folder = 'D:\\IMAGENES SATELITALES\\INAIGEM\\S2A_MSIL1C_20160529T152642_N0202_R025_T17LRL_20160529T153426.SAFE\\GRANULE\\L1C_T17LRL_A004884_20160529T153426\\IMG_DATA'
image = os.path.join(folder, 'T17LRL_20160529T152642_B11.jp2')

with rasterio.open(image, driver='JP2OpenJPEG') as dataset:

    print(dataset.meta)

    # resample data to target shape
    data = dataset.read(
        out_shape=(
            dataset.count,
            int(dataset.height * upscale_factor),
            int(dataset.width * upscale_factor)
        ),
        resampling=Resampling.bilinear
    )

    # scale image transform
    transform = dataset.transform * dataset.transform.scale(
        (dataset.width / data.shape[-1]),
        (dataset.height / data.shape[-2])
    )

    print(transform)

    # write data to new file
    with rasterio.open('T17LRL_20160529T152642_B11_upscaled.jp2', 'w', driver='JP2OpenJPEG',
                       width=data.shape[-1], height=data.shape[-2], count=data.shape[0],
                       crs=dataset.crs, transform=transform, dtype=data.dtype) as out:
        out.write(data)
