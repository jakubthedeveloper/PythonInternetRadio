import atexit
import argparse
from mpc import Mpc
from web_ui import WebUi

class Radio:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Application for checking and informing arduino if there are unread messages on imap mailbox.")
        parser.add_argument("--host", default="0.0.0.0", help="Web ui host")
        parser.add_argument("--port", default=1234, help="Web ui port")
        args = parser.parse_args()

        self.mpc = Mpc()
        atexit.register(self.exitHandler)
        self.webUi = WebUi(self.mpc, args.host, args.port)

    def exitHandler(self):
        self.mpc.stop()
        self.mpc.clear()

radio = Radio()
