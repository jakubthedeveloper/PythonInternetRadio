import subprocess
import atexit
from flask import Flask
from flask import render_template
from flask import request
from yaml import load, dump

stationsFile = open("stations.yml", 'r')
data = load(stationsFile)

stations = []

for k in data:
    print(k)
    stations.append({
        "name": k,
        "url": data[k]
    })

def mpcCommand(cmd):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	return p.stdout.read()

def exitHandler():
    mpcCommand(['mpc', 'stop'])
    mpcCommand(['mpc', 'clear'])

atexit.register(exitHandler)

currentStationUrl = None
app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def control_page(title='Radio control'):
    global currentStationUrl

    if request.method == 'POST':
        if request.form['submit'] == 'Play':
            currentStationUrl = str(request.form['station'])
            mpcCommand(['mpc', 'clear'])
            mpcCommand(['mpc', 'add', currentStationUrl])
            mpcCommand(['mpc', 'play'])
        elif request.form['submit'] == 'Stop':
            mpcCommand(['mpc', 'stop'])

    return render_template('/control.html', title=title, stations=stations, currentStationUrl=currentStationUrl)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
