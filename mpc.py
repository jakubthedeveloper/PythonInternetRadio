import subprocess

class Mpc:
    def mpcCommand(self, cmd):
    	p = subprocess.Popen(['mpc'] + cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    	return p.stdout.read()

    def play(self, url):
        self.clear()
        self.addStation(url)
        self.mpcCommand(["play"])

    def stop(self):
        self.mpcCommand(["stop"])

    def clear(self):
        self.mpcCommand(["clear"])

    def addStation(self, url):
        self.mpcCommand(["add", url])

    def volumeDecrease(self):
        self.mpcCommand(["volume", "-1"])

    def volumeIncrease(self):
        self.mpcCommand(["volume", "+1"])

    def volumeDecreaseFast(self):
        self.mpcCommand(["volume", "-15"])

    def volumeIncreaseFast(self):
        self.mpcCommand(["volume", "+15"])
