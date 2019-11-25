import subprocess

class Mpc:
    def mpcCommand(self, cmd):
    	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    	return p.stdout.read()

    def play(self, url):
        self.clear()
        self.addStation(url)
        self.mpcCommand(["mpc", "play"])

    def stop(self):
        self.mpcCommand(["mpc", "stop"])

    def clear(self):
        self.mpcCommand(["mpc", "clear"])

    def addStation(self, url):
        self.mpcCommand(["mpc", "add", url])
