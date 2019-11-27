import subprocess

class BluetoothService:
    bluetoothSpeakerDevice = None

    def __init__(self):
        None

    def setDevice(self, device):
        self.bluetoothSpeakerDevice = device

    def pair(self):
        if self.bluetoothSpeakerDevice is not None:
            cmd = 'echo -e "power on\nconnect ' + self.bluetoothSpeakerDevice + ' \n quit \n" | /usr/bin/bluetoothctl'
            subprocess.call(cmd, shell=True)

class BluetoothServiceFactory:
    instance = None

    def getService():
        if BluetoothServiceFactory.instance is None:
            BluetoothServiceFactory.instance = BluetoothService()

        return BluetoothServiceFactory.instance
