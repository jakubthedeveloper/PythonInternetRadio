from flask import Flask
from flask import render_template
from flask import request
from stations_service import StationsServiceFactory

class WebUi:
    def __init__(self, mpc, host, port):
        self.stationsService = StationsServiceFactory.getService()

        app = Flask(__name__, template_folder="template")

        @app.route("/", methods=["GET", "POST"])
        def control_page(title="Radio control"):
            if request.method == "POST":
                if request.form["submit"] == "Play":
                    self.stationsService.currentStationIndex = int(request.form["station"])
                    currentStation = self.stationsService.getCurrentStation()

                    if currentStation is not None:
                        mpc.play(currentStation.get('url'))
                elif request.form["submit"] == "Stop":
                    mpc.stop()

            return render_template(
                "/control.html",
                title=title,
                stations=self.stationsService.getStations(),
                currentStationIndex=self.stationsService.currentStationIndex
            )

        app.run(host=host, port=port)
