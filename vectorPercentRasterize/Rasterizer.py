import os

import gdal
import numpy as np

import BdotClass
import County
import PathsManager
import Tile


class Rasterizer:
    inputRaster = ''
    percent = 0
    outputRaster = ''
    workdir = ''
    gdalRasterizePath = ''
    gdalTranslatePath = ''
    gdalTindexPath = ''
    temp1percentRasterPath = ''
    tempSum1percentRasterPath = ''
    tempNormalRasterPath = ''
    resultPath = ''
    bdotMainDirPath = ''
    BdotClasses = []
    tiles = []
    outputCommandsFilePath = ''
    outputCommandsFileHandle = 0
    currentReferenceTif = None
    currentTile = None

    def __init__(self, gdalDirPath):
        self.gdalRasterizePath = gdalDirPath + '/gdal_rasterize'
        self.gdalTranslatePath = gdalDirPath + '/gdal_translate'
        self.gdalTindexPath = gdalDirPath + '/gdaltindex'
        self.fillBdotClasses()
        self.fillTilesWithCounties()

    def fillBdotClasses(self):
        self.BdotClasses.append(BdotClass.BdotClass('BUBD', 1))

        self.BdotClasses.append(BdotClass.BdotClass('BUCM', 21))
        self.BdotClasses.append(BdotClass.BdotClass('BUSP', 21))
        self.BdotClasses.append(BdotClass.BdotClass('KUKO', 21))
        self.BdotClasses.append(BdotClass.BdotClass('OIKM', 21))
        self.BdotClasses.append(BdotClass.BdotClass('PTKM', 21))
        self.BdotClasses.append(BdotClass.BdotClass('PTPL', 21))
        self.BdotClasses.append(BdotClass.BdotClass('BUIB', 21))

        self.BdotClasses.append(BdotClass.BdotClass('OIMK', 20))
        self.BdotClasses.append(BdotClass.BdotClass('OISZ', 20))
        self.BdotClasses.append(BdotClass.BdotClass('PTLZ', 20))
        self.BdotClasses.append(BdotClass.BdotClass('PTRK', 20))
        self.BdotClasses.append(BdotClass.BdotClass('PTTR', 20))
        self.BdotClasses.append(BdotClass.BdotClass('PTUT', 20))
        self.BdotClasses.append(BdotClass.BdotClass('KUKO', 20, "RODZAJ='parking'"))

    def fillTilesWithCounties(self):
        self.tiles.append(Tile.Tile('34UED', "N:/BAMS/CaleMazowsze/training/34UED/training41_1_BUBD_75perc_mean_NDVI_LT_160_mean_RED_seg2_rec.tif"))
        self.tiles[-1].addCounty(County.County('1408'))
        self.tiles[-1].addCounty(County.County('1411'))
        self.tiles[-1].addCounty(County.County('1412'))
        self.tiles[-1].addCounty(County.County('1415'))
        self.tiles[-1].addCounty(County.County('1416'))
        self.tiles[-1].addCounty(County.County('1422'))
        self.tiles[-1].addCounty(County.County('1424'))
        self.tiles[-1].addCounty(County.County('1426'))
        self.tiles[-1].addCounty(County.County('1429'))
        self.tiles[-1].addCounty(County.County('1433'))
        self.tiles[-1].addCounty(County.County('1434'))
        self.tiles[-1].addCounty(County.County('1435'))
        self.tiles[-1].addCounty(County.County('1461'))
        self.tiles[-1].addCounty(County.County('1465'))

        self.tiles.append(Tile.Tile('34UCD', "F:/MarcinRybicki/projects/BAMS/rasterize/workspace/34UCD.tif"))
        self.tiles[-1].addCounty(County.County('1404'))
        self.tiles[-1].addCounty(County.County('1419'))
        self.tiles[-1].addCounty(County.County('1427'))
        self.tiles[-1].addCounty(County.County('0461'))
        self.tiles[-1].addCounty(County.County('0463'))
        self.tiles[-1].addCounty(County.County('0464'))
        self.tiles[-1].addCounty(County.County('0401'))
        self.tiles[-1].addCounty(County.County('0402'))
        self.tiles[-1].addCounty(County.County('0405'))
        self.tiles[-1].addCounty(County.County('0407'))
        self.tiles[-1].addCounty(County.County('0408'))
        self.tiles[-1].addCounty(County.County('0411'))
        self.tiles[-1].addCounty(County.County('0412'))
        self.tiles[-1].addCounty(County.County('0415'))
        self.tiles[-1].addCounty(County.County('0418'))
        self.tiles[-1].addCounty(County.County('1002'))

        self.tiles.append(Tile.Tile('34UDB', "N:/BAMS/CaleMazowsze/training/34UDB/training_34UDB_rec.tif"))
        self.tiles[-1].addCounty(County.County('1423'))
        self.tiles[-1].addCounty(County.County('1425'))
        self.tiles[-1].addCounty(County.County('1430'))
        self.tiles[-1].addCounty(County.County('1463'))
        self.tiles[-1].addCounty(County.County('1062'))
        self.tiles[-1].addCounty(County.County('1007'))
        self.tiles[-1].addCounty(County.County('1010'))
        self.tiles[-1].addCounty(County.County('1012'))
        self.tiles[-1].addCounty(County.County('2661'))
        self.tiles[-1].addCounty(County.County('2601'))
        self.tiles[-1].addCounty(County.County('2602'))
        self.tiles[-1].addCounty(County.County('2604'))
        self.tiles[-1].addCounty(County.County('2605'))
        self.tiles[-1].addCounty(County.County('2608'))
        self.tiles[-1].addCounty(County.County('2610'))
        self.tiles[-1].addCounty(County.County('2611'))
        self.tiles[-1].addCounty(County.County('2613'))

        self.tiles.append(Tile.Tile('34UDC', "N:/BAMS/CaleMazowsze/training/34UDC/training_34UDC_rec.tif"))
        self.tiles[-1].addCounty(County.County('1401'))
        self.tiles[-1].addCounty(County.County('1405'))
        self.tiles[-1].addCounty(County.County('1406'))
        self.tiles[-1].addCounty(County.County('1418'))
        self.tiles[-1].addCounty(County.County('1421'))
        self.tiles[-1].addCounty(County.County('1423'))
        self.tiles[-1].addCounty(County.County('1425'))
        self.tiles[-1].addCounty(County.County('1428'))
        self.tiles[-1].addCounty(County.County('1432'))
        self.tiles[-1].addCounty(County.County('1438'))
        self.tiles[-1].addCounty(County.County('1463'))
        self.tiles[-1].addCounty(County.County('1465'))
        self.tiles[-1].addCounty(County.County('1062'))
        self.tiles[-1].addCounty(County.County('1063'))
        self.tiles[-1].addCounty(County.County('1005'))
        self.tiles[-1].addCounty(County.County('1013'))
        self.tiles[-1].addCounty(County.County('1015'))
        self.tiles[-1].addCounty(County.County('1016'))

        self.tiles.append(Tile.Tile('34UDD', "N:/BAMS/CaleMazowsze/training/34UDD/training_34UDD_rec.tif"))
        self.tiles[-1].addCounty(County.County('1402'))
        self.tiles[-1].addCounty(County.County('1404'))
        self.tiles[-1].addCounty(County.County('1408'))
        self.tiles[-1].addCounty(County.County('1411'))
        self.tiles[-1].addCounty(County.County('1413'))
        self.tiles[-1].addCounty(County.County('1414'))
        self.tiles[-1].addCounty(County.County('1419'))
        self.tiles[-1].addCounty(County.County('1420'))
        self.tiles[-1].addCounty(County.County('1422'))
        self.tiles[-1].addCounty(County.County('1424'))
        self.tiles[-1].addCounty(County.County('1427'))
        self.tiles[-1].addCounty(County.County('1428'))
        self.tiles[-1].addCounty(County.County('1432'))
        self.tiles[-1].addCounty(County.County('1437'))
        self.tiles[-1].addCounty(County.County('1462'))
        self.tiles[-1].addCounty(County.County('1465'))

        self.tiles.append(Tile.Tile('34UDE', "N:/BAMS/CaleMazowsze/training/34UDE/training_34UDE_rec.tif"))
        self.tiles[-1].addCounty(County.County('1413'))
        self.tiles[-1].addCounty(County.County('1422'))
        self.tiles[-1].addCounty(County.County('1437'))
        self.tiles[-1].addCounty(County.County('0402'))
        self.tiles[-1].addCounty(County.County('2862'))
        self.tiles[-1].addCounty(County.County('2803'))
        self.tiles[-1].addCounty(County.County('2804'))
        self.tiles[-1].addCounty(County.County('2807'))
        self.tiles[-1].addCounty(County.County('2809'))
        self.tiles[-1].addCounty(County.County('2811'))
        self.tiles[-1].addCounty(County.County('2812'))
        self.tiles[-1].addCounty(County.County('2814'))
        self.tiles[-1].addCounty(County.County('2815'))
        self.tiles[-1].addCounty(County.County('2817'))

        self.tiles.append(Tile.Tile('34UEB', "N:/BAMS/CaleMazowsze/training/34UEB/training_34UEB_rec.tif"))
        self.tiles[-1].addCounty(County.County('1409'))
        self.tiles[-1].addCounty(County.County('1425'))
        self.tiles[-1].addCounty(County.County('1430'))
        self.tiles[-1].addCounty(County.County('1436'))
        self.tiles[-1].addCounty(County.County('1463'))
        self.tiles[-1].addCounty(County.County('0663'))
        self.tiles[-1].addCounty(County.County('0605'))
        self.tiles[-1].addCounty(County.County('0607'))
        self.tiles[-1].addCounty(County.County('0609'))
        self.tiles[-1].addCounty(County.County('0612'))
        self.tiles[-1].addCounty(County.County('0614'))
        self.tiles[-1].addCounty(County.County('2606'))
        self.tiles[-1].addCounty(County.County('2607'))
        self.tiles[-1].addCounty(County.County('2609'))
        self.tiles[-1].addCounty(County.County('2611'))
        self.tiles[-1].addCounty(County.County('2612'))

        self.tiles.append(Tile.Tile('34UEC', "N:/BAMS/CaleMazowsze/training/34UEC/training_34UEC_rec.tif"))
        self.tiles[-1].addCounty(County.County('1401'))
        self.tiles[-1].addCounty(County.County('1403'))
        self.tiles[-1].addCounty(County.County('1406'))
        self.tiles[-1].addCounty(County.County('1407'))
        self.tiles[-1].addCounty(County.County('1412'))
        self.tiles[-1].addCounty(County.County('1417'))
        self.tiles[-1].addCounty(County.County('1418'))
        self.tiles[-1].addCounty(County.County('1425'))
        self.tiles[-1].addCounty(County.County('1426'))
        self.tiles[-1].addCounty(County.County('1433'))
        self.tiles[-1].addCounty(County.County('1434'))
        self.tiles[-1].addCounty(County.County('1436'))
        self.tiles[-1].addCounty(County.County('1463'))
        self.tiles[-1].addCounty(County.County('1464'))
        self.tiles[-1].addCounty(County.County('1465'))
        self.tiles[-1].addCounty(County.County('0611'))
        self.tiles[-1].addCounty(County.County('0614'))
        self.tiles[-1].addCounty(County.County('0616'))

        self.tiles.append(Tile.Tile('34UEE', "N:/BAMS/CaleMazowsze/training/34UEE/training_34UEE_rec.tif"))
        self.tiles[-1].addCounty(County.County('1415'))
        self.tiles[-1].addCounty(County.County('1422'))
        self.tiles[-1].addCounty(County.County('2062'))
        self.tiles[-1].addCounty(County.County('2004'))
        self.tiles[-1].addCounty(County.County('2006'))
        self.tiles[-1].addCounty(County.County('2007'))
        self.tiles[-1].addCounty(County.County('2805'))
        self.tiles[-1].addCounty(County.County('2806'))
        self.tiles[-1].addCounty(County.County('2810'))
        self.tiles[-1].addCounty(County.County('2816'))
        self.tiles[-1].addCounty(County.County('2817'))

        self.tiles.append(Tile.Tile('34UFC', "N:/BAMS/CaleMazowsze/training/34UFC/training_34UFC_rec.tif"))
        self.tiles[-1].addCounty(County.County('1410'))
        self.tiles[-1].addCounty(County.County('1426'))
        self.tiles[-1].addCounty(County.County('0661'))
        self.tiles[-1].addCounty(County.County('0601'))
        self.tiles[-1].addCounty(County.County('0608'))
        self.tiles[-1].addCounty(County.County('0611'))
        self.tiles[-1].addCounty(County.County('0613'))
        self.tiles[-1].addCounty(County.County('0615'))
        self.tiles[-1].addCounty(County.County('0619'))

        self.tiles.append(Tile.Tile('34UFD', "N:/BAMS/CaleMazowsze/training/34UFD/training_34UFD_rec.tif"))
        self.tiles[-1].addCounty(County.County('1410'))
        self.tiles[-1].addCounty(County.County('1426'))
        self.tiles[-1].addCounty(County.County('2061'))
        self.tiles[-1].addCounty(County.County('2002'))
        self.tiles[-1].addCounty(County.County('2003'))
        self.tiles[-1].addCounty(County.County('2005'))
        self.tiles[-1].addCounty(County.County('2010'))
        self.tiles[-1].addCounty(County.County('2013'))

    def prepareData(self, workdir, inputRaster, bdotMainDirPath, percent, outputRaster):
        self.workdir = workdir
        self.inputRaster = inputRaster
        self.bdotMainDirPath = bdotMainDirPath
        self.percent = percent
        self.outputRaster = outputRaster
        self.temp1percentRasterPath = self.workdir + '/temp1p.tif'
        self.tempSum1percentRasterPath = self.workdir + '/tempSum1p.tif'
        self.tempNormalRasterPath = self.workdir + '/tempNormal.tif'
        self.outputCommandsFilePath = self.workdir + '/commands.txt'
        self.outputCommandsFileHandle = open(self.outputCommandsFilePath, "w")
        #TODO: check files exists, create no existing dirs

    def doRasterize(self):
        for t in self.tiles:
            self.currentTile = t
            self.doRasterizeForTile(t)
            #return
        self.outputCommandsFileHandle.close()

    def doRasterizeForTile(self, tile):
        self.resultPath = self.workdir + '/trainingRaster_' + tile.name + '.tif'
        self.currentReferenceTif = tile.exampleImage
        print('create1PercentImage')
        self.create1PercentImage(tile.exampleImage)
        print('rasterizeTileOn1percentImage')
        self.rasterizeTileOn1percentImage(tile)
        print('sumDownsamplingRasterizedImage')
        self.sumDownsamplingRasterizedImage()
        print('createNormalImage')
        self.createNormalImage(tile.exampleImage)
        print('rasterizeTileOnNormalImage')
        self.rasterizeTileOnNormalImage(tile)
        print('combineRasterizedImages')
        self.combineRasterizedImages()
        self.clearTempData()

    def create1PercentImage(self, inputRaster):
        #TODO: chcange rigid 1 1 in metres for auto
        command = self.gdalTranslatePath + ' ' '-tr 1 1 -ot Byte -co "COMPRESS=LZW" ' + inputRaster + ' ' + self.temp1percentRasterPath
        self.runSystemProcess(command)
        self.zeros1PercentImage()

    def createNormalImage(self, inputRaster):
        command = self.gdalTranslatePath + ' -ot Byte -co "COMPRESS=LZW" ' + inputRaster + ' ' + self.tempNormalRasterPath
        self.runSystemProcess(command)
        self.zerosNormalImage()

    def zeros1PercentImage(self):
        framePath = self.workdir + '/frame.shp'
        command = self.gdalTindexPath + ' ' + framePath + ' ' + self.temp1percentRasterPath
        self.runSystemProcess(command)
        self.burnShpOn1percentImage(framePath, 0)
        os.remove(framePath)

    def zerosNormalImage(self):
        framePath = self.workdir + '/frame.shp'
        command = self.gdalTindexPath + ' ' + framePath + ' ' + self.tempNormalRasterPath
        self.runSystemProcess(command)
        self.burnShpOnNormalImage(framePath, 0)
        os.remove(framePath)

    def burnShpOn1percentImage(self, shpPath, value, detailedQuery=''):
        command = self.gdalRasterizePath + ' -burn ' + str(value)
        if len(detailedQuery) > 0:
            command = command + ' -where "' + detailedQuery + '"'
        command = command + ' ' + shpPath + ' ' + self.temp1percentRasterPath
        self.runSystemProcess(command)

    def burnShpOnNormalImage(self, shpPath, value, detailedQuery=''):
        command = self.gdalRasterizePath + ' -burn ' + str(value)
        if len(detailedQuery) > 0:
            command = command + ' -where "' + detailedQuery + '"'
        command = command + ' ' + shpPath + ' ' + self.tempNormalRasterPath
        self.runSystemProcess(command)

    def rasterizeTileOn1percentImage(self, tile):
        for county in tile.counties:
            for bdotClass in self.BdotClasses:
                if bdotClass.number == 1:
                    shpFile = PathsManager.FindShpFileForCountyAndClass(self.bdotMainDirPath, county, bdotClass)
                    self.burnShpOn1percentImage(shpFile, bdotClass.number, bdotClass.detailedQuery)

    def rasterizeTileOnNormalImage(self, tile):
        for county in tile.counties:
            for bdotClass in self.BdotClasses:
                if bdotClass.number != 1:
                    shpFile = PathsManager.FindShpFileForCountyAndClass(self.bdotMainDirPath, county, bdotClass)
                    self.burnShpOnNormalImage(shpFile, bdotClass.number, bdotClass.detailedQuery)

    def clearTempData(self):
        command = "del /f " + self.temp1percentRasterPath
        self.runSystemProcess(command)
        #os.remove(self.temp1percentRasterPath)

    def runSystemProcess(self, command):
        #TODO
        if not self.outputCommandsFileHandle.closed:
            self.outputCommandsFileHandle.write(command)
            self.outputCommandsFileHandle.write('\n')
        #print(command)
        os.system((command))

    def sumDownsamplingRasterizedImage(self):
        img = self.readRaster(self.temp1percentRasterPath.replace('/', '\\'))
        img[img == 255] = 0
        H, W = img.shape
        wh = 10
        ww = 10
        imgReshaped = img.reshape(int(H/wh), wh, int(W/ww), ww)
        img = None
        resultSummed = np.einsum('ijkl->ik', imgReshaped)
        imgReshaped = None
        #thresholding:
        dst_filename = self.tempSum1percentRasterPath + self.currentTile.name + 'Percent.tif'
        driver = gdal.GetDriverByName("GTiff")
        referenceDataSet = gdal.Open(self.currentReferenceTif, gdal.GA_ReadOnly)
        self.geotransform = referenceDataSet.GetGeoTransform()
        self.projection = referenceDataSet.GetProjection()
        dst_ds = driver.Create(dst_filename, xsize=int(W/ww), ysize=int(H/wh), bands=1, eType=gdal.GDT_Byte)
        dst_ds.SetGeoTransform(self.geotransform)
        dst_ds.SetProjection(self.projection)
        dst_ds.GetRasterBand(1).WriteArray(resultSummed)

        resultSummed[resultSummed <= self.percent] = 0
        resultSummed[resultSummed > self.percent] = 1

        dst_filename = self.tempSum1percentRasterPath
        dst_ds = driver.Create(dst_filename, xsize=int(W / ww), ysize=int(H / wh), bands=1, eType=gdal.GDT_Byte)
        dst_ds.SetGeoTransform(self.geotransform)
        dst_ds.SetProjection(self.projection)
        dst_ds.GetRasterBand(1).WriteArray(resultSummed)

        dst_ds = None

    def readRaster(self, rasterPath):
        #rasterPath = "F:/MarcinRybicki/codes/BAMS/vectorPercentRasterize/workdir/wycinek/tempWycinek.tif"
        dataset = gdal.Open(rasterPath, gdal.GA_ReadOnly)
        if not dataset:
            print("Cannot open " + rasterPath)
        band = dataset.GetRasterBand(1)
        wholeImage = band.ReadAsArray(xoff=0, yoff=0, win_xsize=band.XSize, win_ysize=band.YSize)

        return wholeImage

    def combineRasterizedImages(self):
        summedImage = self.readRaster(self.tempSum1percentRasterPath)
        normalImage = self.readRaster(self.tempNormalRasterPath)
        normalImage[summedImage == 1] = 1
        summedImage = None
        driver = gdal.GetDriverByName("GTiff")
        dst_filename =self.resultPath
        dst_ds = driver.Create(dst_filename, xsize=int(10980), ysize=int(10980), bands=1, eType=gdal.GDT_Byte)
        dst_ds.SetGeoTransform(self.geotransform)
        dst_ds.SetProjection(self.projection)
        dst_ds.GetRasterBand(1).WriteArray(normalImage)
        dst_ds = None
