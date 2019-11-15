Save QGIS Style image as one-layer raster image.

**First step:**
Convert QGIS Style (in .qml) to .txt file.
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

**Example 1:**
```bash
[root@localhost sf_qgis-api]# gdaldem color-relief input-1.tif gdal-colors.txt output-1.tif
0...10...20...30...40...50...60...70...80...90...100 - done.
[root@localhost sf_qgis-api]#
```
| input-1.tif | output-1.tif |
| :------------ | :------------ |
![input-1.tif](https://github.com/lazyspot/gdal-tools/blob/master/qgis-style-save-as-image/img/input-1.png) | 
![output-1.tif](https://github.com/lazyspot/gdal-tools/blob/master/qgis-style-save-as-image/img/output-1.png) |

**Example 2:**
```bash
[root@localhost sf_qgis-api]# gdaldem color-relief input-2.tif gdal-colors.txt output-2.tif
0...10...20...30...40...50...60...70...80...90...100 - done.
[root@localhost sf_qgis-api]#
```
![input-2.tif](https://github.com/lazyspot/gdal-tools/blob/master/qgis-style-save-as-image/img/input-2.png)
![output-2.tif](https://github.com/lazyspot/gdal-tools/blob/master/qgis-style-save-as-image/img/output-2.png)
