from stations_parser import StationsParser

class StationsService:
    instance = None
    currentIndex = 0
    stations = None
    currentStationUrl = None

    def __init__(self):
        stationsParser = StationsParser()
        self.stations = stationsParser.getStationsFromFile("stations.yml")

    def getStations(self):
        return self.stations

class StationsServiceFactory:
    instance = None

    def getService():
        if StationsServiceFactory.instance is None:
            StationsServiceFactory.instance = StationsService()

        return StationsServiceFactory.instance
