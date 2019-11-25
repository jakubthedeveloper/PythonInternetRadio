from flask import Flask
from flask import render_template
from flask import request
from stations_parser import StationsParser

class WebUi:
    def __init__(self, mpc, host, port):
        stationsParser = StationsParser()
        stations = stationsParser.getStationsFromFile("stations.yml")
        app = Flask(__name__, template_folder="template")
        self.currentStationUrl = None

        @app.route("/", methods=["GET", "POST"])
        def control_page(title="Radio control"):
            if request.method == "POST":
                if request.form["submit"] == "Play":
                    self.currentStationUrl = str(request.form["station"])
                    mpc.play(self.currentStationUrl)
                elif request.form["submit"] == "Stop":
                    mpc.stop()

            return render_template("/control.html", title=title, stations=stations, currentStationUrl=self.currentStationUrl)

        app.run(host=host, port=port)
