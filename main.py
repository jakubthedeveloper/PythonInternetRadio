import atexit
import argparse
from mpc import Mpc
from web_ui import WebUi
from bluetooth_service import BluetoothServiceFactory

class Radio:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Internet radio with Web interface for Linux or Raspbian.")
        parser.add_argument("--host", default="0.0.0.0", help="Web ui host")
        parser.add_argument("--port", default=1234, help="Web ui port")
        parser.add_argument("--bluetooth-speaker-device", help="Bluetooth device identifier (taken from bluetoothctl)")
        parser.add_argument("--show-volume-controls", default="yes", choices=["yes", "no"], help="Show volume controls, choices: yes / no,  default: yes")
        args = parser.parse_args()

        self.mpc = Mpc()
        BluetoothServiceFactory.getService().setDevice(args.bluetooth_speaker_device)
        atexit.register(self.exitHandler)
        self.webUi = WebUi(
            self.mpc,
            args.host,
            args.port,
            args.bluetooth_speaker_device is not None,
            args.show_volume_controls == "yes"
        )

    def exitHandler(self):
        self.mpc.stop()
        self.mpc.clear()

radio = Radio()
