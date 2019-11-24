import subprocess
import atexit
from flask import Flask
from flask import render_template
from flask import request
import oyaml as yaml
import argparse

class Radio:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Application for checking and informing arduino if there are unread messages on imap mailbox.")
        parser.add_argument("--host", default="0.0.0.0", help="Web ui host")
        parser.add_argument("--port", default=1234, help="Web ui port")
        args = parser.parse_args()

        self.host = args.host
        self.port = args.port

        stationsFile = open("stations.yml", "r")
        data = yaml.load(stationsFile)

        self.stations = []
        self.currentStationUrl = None

        for k in data:
            self.stations.append({
                "name": k,
                "url": data[k]
            })

        atexit.register(self.exitHandler)
        self.initWebUi()

    def mpcCommand(self, cmd):
    	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    	return p.stdout.read()

    def exitHandler(self):
        self.mpcCommand(["mpc", "stop"])
        self.mpcCommand(["mpc", "clear"])


    def initWebUi(self):
        app = Flask(__name__, template_folder="template")

        @app.route("/", methods=["GET", "POST"])
        def control_page(title="Radio control"):
            if request.method == "POST":
                if request.form["submit"] == "Play":
                    self.currentStationUrl = str(request.form["station"])
                    self.mpcCommand(["mpc", "clear"])
                    self.mpcCommand(["mpc", "add", self.currentStationUrl])
                    self.mpcCommand(["mpc", "play"])
                elif request.form["submit"] == "Stop":
                    self.mpcCommand(["mpc", "stop"])

            return render_template("/control.html", title=title, stations=self.stations, currentStationUrl=self.currentStationUrl)

        app.run(host=self.host, port=self.port)

radio = Radio()
