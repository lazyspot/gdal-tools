Save QGIS Style image as one-layer raster image.

First step:
Convert QGIS Style (in .qml) to .txt file.
Example



GDAL command:
```bash
gdaldem color-relief inputfile color_table.txt outputfile
```

Example:

```bash
gdaldem color-relief inputfile.tif color_table.txt outputfile.tif
```