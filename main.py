import atexit
import argparse
from mpc import Mpc
from web_ui import WebUi

class Radio:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Application for checking and informing arduino if there are unread messages on imap mailbox.")
        parser.add_argument("--host", default="0.0.0.0", help="Web ui host")
        parser.add_argument("--port", default=1234, help="Web ui port")
        parser.add_argument("--bluetooth-speaker-device", help="Bluetooth device identifier (taken from bluetoothctl)")
        args = parser.parse_args()

        self.mpc = Mpc()
        atexit.register(self.exitHandler)
        self.webUi = WebUi(self.mpc, args.host, args.port, args.bluetooth_speaker_device)

    def exitHandler(self):
        self.mpc.stop()
        self.mpc.clear()

radio = Radio()
