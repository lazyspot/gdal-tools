import gdal

option = gdal.DEMProcessingOptions(band=1,
                                   colorFilename="gdal-colors.txt")
gdal.DEMProcessing(processing="color-relief", srcDS="input-1.tif", destName="output-1.tif",
                   options=option)
                   
option = gdal.DEMProcessingOptions(band=1,
                                   colorFilename="gdal-colors.txt")
gdal.DEMProcessing(processing="color-relief", srcDS="input-2.tif", destName="output-2.tif",
                   options=option)