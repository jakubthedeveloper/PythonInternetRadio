from stations_parser import StationsParser

class StationsService:
    instance = None

    stations = None
    currentStationIndex = None

    def __init__(self):
        stationsParser = StationsParser()
        self.stations = stationsParser.getStationsFromFile("stations.yml")

    def getStations(self):
        return self.stations

    def getCurrentStation(self):
        if self.currentStationIndex is None or self.currentStationIndex < 0 or self.currentStationIndex >= len(self.stations):
            return None

        return self.stations[self.currentStationIndex]

class StationsServiceFactory:
    instance = None

    def getService():
        if StationsServiceFactory.instance is None:
            StationsServiceFactory.instance = StationsService()

        return StationsServiceFactory.instance
