import glob
import os

def FindPathsWithWildcard(mainDir, wildcard):
    foundPaths = []
    fullWildCard = mainDir + '/*/' +wildcard
    listing = glob.glob(fullWildCard)
    for filename in listing:
        foundPaths.append(filename)
    return foundPaths

def FindDirPathsWithWildcard(mainDir, wildcard):
    foundPaths = FindPathsWithWildcard(mainDir, wildcard);
    foundDirs = []
    for p in foundPaths:
        if os.path.isdir(p):
            foundDirs.append(p)
    return foundDirs

def FindFilePathsWithWildcard(mainDir, wildcard):
    foundPaths = FindPathsWithWildcard(mainDir, wildcard);
    foundFiles = []
    for p in foundPaths:
        if os.path.isfile(p):
            foundFiles.append(p)
    return foundFiles


def FindShpFileForCountyAndClass(bdotMainDir, county, bdotClass):
    foundPath = ''
    wildcard = '*'+ county.BDOTnumber + '*' + bdotClass.name + '*.shp'
    foundPaths = FindFilePathsWithWildcard(bdotMainDir, wildcard)
    if len(foundPaths) > 0:
        foundPath = foundPaths[0]
    return foundPath