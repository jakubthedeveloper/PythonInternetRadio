import oyaml as yaml

class StationsParser:
    def getStationsFromFile(self, fileName):
        stationsFile = open(fileName, "r")

        results = self.getStationsFromYaml(
            yaml.load(stationsFile, Loader=yaml.BaseLoader)
        )

        stationsFile.close()
        return results

    def getStationsFromYaml(self, data):
        stations = []

        for k in data:
            stations.append({
                "name": k,
                "url": data[k]
            })

        return stations
