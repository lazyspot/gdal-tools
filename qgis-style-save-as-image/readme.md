## Convert single band raster to RGB image with costumized style

### Using images with constats values.

This is methods for image with constans values. One value for exactly only one color.

#### **First step:**
Example with QGIS:
Convert QGIS Style (in .qml) to .txt file.
This step must be performed by yourself.
You can use online converters (e.g. https://www.rapidtables.com/convert/color/hex-to-rgb.html).

Example (**qgis-style.qml**)
```xml
<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.18.2" minimumScale="inf" maximumScale="1e+08" hasScaleBasedVisibilityFlag="0">
  <pipe>
    <rasterrenderer opacity="1" alphaBand="-1" classificationMax="162" classificationMinMaxOrigin="CumulativeCutFullExtentEstimated" band="1" classificationMin="5" type="singlebandpseudocolor">
      <rasterTransparency/>
      <rastershader>
        <colorrampshader colorRampType="INTERPOLATED" clip="0">
          <item alpha="255" value="0" label="Clouds" color="#ffffff"/>
          <item alpha="255" value="62" label="Artificial surfaces and constructions" color="#d20000"/>
          <item alpha="255" value="73" label="Cultivated areas" color="#fdd327"/>
          <item alpha="255" value="75" label="Vineyards" color="#b05b10"/>
          <item alpha="255" value="82" label="Broadleaf tree cover" color="#239800"/>
          <item alpha="255" value="83" label="Coniferous tree cover" color="#086200"/>
          <item alpha="255" value="102" label="Herbaceous vegetation" color="#f99627"/>
          <item alpha="255" value="103" label="Moors and Heathland" color="#8d8b00"/>
          <item alpha="255" value="104" label="Sclerophyllous vegetation" color="#5f3506"/>
          <item alpha="255" value="105" label="Marshes" color="#956bc4"/>
          <item alpha="255" value="106" label="Peatbogs" color="#4d256a"/>
          <item alpha="255" value="121" label="Natural material surfaces" color="#9a9a9a"/>
          <item alpha="255" value="123" label="Permanent snow covered surfaces" color="#6affff"/>
          <item alpha="255" value="162" label="Water bodies" color="#1445f9"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" colorizeRed="255" colorizeBlue="128" grayscaleMode="0" saturation="0" colorizeStrength="100"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

```
Converted to txt (**gdal-colors.txt**):
```txt
0: 255 255 255 255
62: 210 0 0 255
73: 253 211 39 255
75: 176 91 16 255
82: 35 152 0 255
83: 8 98 0 255
102: 249 150 39 255
103: 141 139 0 255
104: 95 53 6 255
105: 149 107 196 255
106: 77 37 106 255
121: 154 154 154 255
123: 106 255 255 255
162: 20 69 249 255
```

#### **Description:**

|   Color   |   Value   |   Red   |   Green   |   Blue   |   Alpha   |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
|   ![#ffffff](/qgis-style-save-as-image/img/colors/ffffff-65x25.png)   |   0:   |   255   |   255   |   255   |   255   |
|   ![#d20000](/qgis-style-save-as-image/img/colors/d20000-65x25.png)   |   62:   |   210   |   0   |   0   |   255   |
|   ![#fdd327](/qgis-style-save-as-image/img/colors/fdd327-65x25.png)   |   73:   |   253   |   211   |   39   |   255   |
|   ![#b05b10](/qgis-style-save-as-image/img/colors/b05b10-65x25.png)   |   75:   |   176   |   91   |   16   |   255   |
|   ![#239800](/qgis-style-save-as-image/img/colors/239800-65x25.png)   |   82:   |   35   |   152   |   0   |   255   |
|   ![#086200](/qgis-style-save-as-image/img/colors/086200-65x25.png)   |   83:   |   8   |   98   |   0   |   255   |
|   ![#f99627](/qgis-style-save-as-image/img/colors/f99627-65x25.png)   |   102:   |   249   |   150   |   39   |   255   |
|   ![#8d8b00](/qgis-style-save-as-image/img/colors/8d8b00-65x25.png)   |   103:   |   141   |   139   |   0   |   255   |
|   ![#5f3506](/qgis-style-save-as-image/img/colors/5f3506-65x25.png)   |   104:   |   95   |   53   |   6   |   255   |
|   ![#956bc4](/qgis-style-save-as-image/img/colors/956bc4-65x25.png)   |   105:   |   149   |   107   |   196   |   255   |
|   ![#4d256a](/qgis-style-save-as-image/img/colors/4d256a-65x25.png)   |   106:   |   77   |   37   |   106   |   255   |
|   ![#9a9a9a](/qgis-style-save-as-image/img/colors/9a9a9a-65x25.png)   |   121:   |   154   |   154   |   154   |   255   |
|   ![#6affff](/qgis-style-save-as-image/img/colors/6affff-65x25.png)   |   123:   |   106   |   255   |   255   |   255   |
|   ![#1445f9](/qgis-style-save-as-image/img/colors/1445f9-65x25.png)   |   162:   |   20   |   69   |   249   |   255   |

**Second step:**
Run gdaldem commamnd with color-relief flag, first argument is input file, second is .txt file with colors the last one is output file.

GDAL command:
```bash
gdaldem color-relief inputfile color_table.txt outputfile
```

**Command:**

```bash
gdaldem color-relief inputfile.tif color_table.txt outputfile.tif
```

Resolution after convertion is the same.

```gdaldem``` documentation:
[https://gdal.org/programs/gdaldem.html](https://gdal.org/programs/gdaldem.html "https://gdal.org/programs/gdaldem.html")

**Example 1:**
```bash
[root@localhost sf_qgis-api]# gdaldem color-relief input-1.tif gdal-colors.txt output-1.tif
0...10...20...30...40...50...60...70...80...90...100 - done.
[root@localhost sf_qgis-api]#
```
| input-1.tif | output-1.tif |
| :------------ | :------------ |
![input-1.tif](https://github.com/lazyspot/gdal-tools/blob/master/qgis-style-save-as-image/img/input-1.png) | ![output-1.tif](https://github.com/lazyspot/gdal-tools/blob/master/qgis-style-save-as-image/img/output-1.png) |

**Example 2:**
```bash
[root@localhost sf_qgis-api]# gdaldem color-relief input-2.tif gdal-colors.txt output-2.tif
0...10...20...30...40...50...60...70...80...90...100 - done.
[root@localhost sf_qgis-api]#
```
| input-2.tif | output-2.tif |
| :------------ | :------------ |
| ![input-2.tif](https://github.com/lazyspot/gdal-tools/blob/master/qgis-style-save-as-image/img/input-2.png) | ![output-2.tif](https://github.com/lazyspot/gdal-tools/blob/master/qgis-style-save-as-image/img/output-2.png) |

### Using images with compartment values.
This type of images have one color to values between two value.


### Using in python


```gdaldem``` have the interface for python:
[https://gdal.org/python/osgeo.gdal-module.html#DEMProcessingOptions](https://gdal.org/python/osgeo.gdal-module.html#DEMProcessingOptions "https://gdal.org/python/osgeo.gdal-module.html#DEMProcessingOptions")

Example in python:

source [gdaldem.py](gdaldem.py)
```python
import gdal

option = gdal.DEMProcessingOptions(band=1,
                                   colorFilename="gdal-colors.txt")
gdal.DEMProcessing(processing="color-relief", srcDS="input-1.tif", destName="output-1.tif",
                   options=option)
                   
option = gdal.DEMProcessingOptions(band=1,
                                   colorFilename="gdal-colors.txt")
gdal.DEMProcessing(processing="color-relief", srcDS="input-2.tif", destName="output-2.tif",
                   options=option)
```