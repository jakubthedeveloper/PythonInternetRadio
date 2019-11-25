import oyaml as yaml

class StationsParser:
    def getStationsFromFile(self, fileName):
        stationsFile = open(fileName, "r")

        return self.getStationsFromYaml(
            yaml.load(stationsFile)
        )

    def getStationsFromYaml(self, data):
        stations = []

        for k in data:
            stations.append({
                "name": k,
                "url": data[k]
            })

        return stations
