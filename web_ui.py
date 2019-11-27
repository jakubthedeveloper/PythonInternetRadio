from flask import Flask
from flask import render_template
from flask import request
from stations_service import StationsServiceFactory
from bluetooth_service import BluetoothServiceFactory

class WebUi:
    def __init__(self, mpc, host, port, showBluetoothControls, showVolumeControls):
        self.stationsService = StationsServiceFactory.getService()

        app = Flask(__name__, template_folder="template")

        @app.route("/", methods=["GET", "POST"])
        def control_page(title="Radio control"):
            if request.method == "POST":
                if request.form["action"] == "play":
                    self.stationsService.currentStationIndex = int(request.form["stationIndex"])
                    currentStation = self.stationsService.getCurrentStation()

                    if currentStation is not None:
                        mpc.play(currentStation.get('url'))
                elif request.form["action"] == "stop":
                    mpc.stop()
                elif request.form["action"] == "volume_decrease":
                    mpc.volumeDecrease()
                elif request.form["action"] == "volume_increase":
                    mpc.volumeIncrease()
                elif request.form["action"] == "volume_decrease_fast":
                    mpc.volumeDecreaseFast()
                elif request.form["action"] == "volume_increase_fast":
                    mpc.volumeIncreaseFast()
                elif request.form["action"] == "pair_bt":
                    BluetoothServiceFactory.getService().pair()

            return render_template(
                "/control.html",
                title=title,
                stations=self.stationsService.getStations(),
                currentStationIndex=self.stationsService.currentStationIndex,
                showBluetoothControls=showBluetoothControls,
                showVolumeControls=showVolumeControls
            )

        app.run(host=host, port=port)
