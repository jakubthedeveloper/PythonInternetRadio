import oyaml as yaml

class StationsParser:
    def getStations(fileName):
        stationsFile = open(fileName, "r")
        data = yaml.load(stationsFile)

        stations = []

        for k in data:
            stations.append({
                "name": k,
                "url": data[k]
            })

        return stations
