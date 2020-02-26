vectorPercentRasterize
======================
A tool for rasterize vectors to use as training data in BAMS project.
Allows to specify a percent threshold to avoid pixels with too small coverage by class.
Works on Sentinel-2 images and BDOT vector database.
Pixel's coverage is calculating with approximation but it is fast. 
At now, it requires to change paths and tile's names in the code.