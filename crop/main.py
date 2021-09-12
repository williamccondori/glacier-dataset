from osgeo import gdal

dem = gdal.Open("D:\\Tesis\\Imágenes satelitales\\IS002\\IS002_GT.tif")

gt = dem.GetGeoTransform()

# get coordinates of upper left corner
xmin = gt[0]
ymax = gt[3]
res = gt[1]

# determine total length of raster
xlen = res * dem.RasterXSize
ylen = res * dem.RasterYSize

# number of tiles in x and y direction
div = 200

xsize = xlen / div
ysize = ylen / div

# loop over min and max x and y coordinates


print(gt)
print(xsize)
print(ysize)
print(div)

for i in range(div):
    for j in range(div):
        output_file = "images/IS002_GT_" + str(i + 1) + str(j + 1) + ".tif"
        xmin = xmin + (xsize * i)
        ymax = ymax - (ysize * j)
        xmax = xmin + 549
        ymin = ymax + 549
        print(xmin)
        print(ymax)
        print(xmax)
        print(ymin)
        gdal.Translate(output_file, dem, outputBounds=(xmax, ymin, xmin, ymax), xRes=res, yRes=-res)

dem = None
