class Tile:
    name = ''
    counties = []
    exampleImage = ''

    def __init__(self, name, exampleImage=''):
        self.name = name
        self.counties = []
        self.exampleImage = exampleImage

    def addCounty(self, county):
        self.counties.append(county)
