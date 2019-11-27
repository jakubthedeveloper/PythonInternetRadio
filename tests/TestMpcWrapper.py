import unittest
from unittest.mock import MagicMock

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from mpc import Mpc

class TestStationsParser(unittest.TestCase):
    def test_play_calls_mpc_play_command(self):
        mpc = Mpc()
        mpc.mpcCommand = MagicMock()

        mpc.play("http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p")
        mpc.mpcCommand.assert_called_with(['play'])

    def test_clear_calls_mpc_clear_command(self):
        mpc = Mpc()
        mpc.mpcCommand = MagicMock()

        mpc.clear()
        mpc.mpcCommand.assert_called_with(['clear'])

    def test_clear_calls_mpc_stop_command(self):
        mpc = Mpc()
        mpc.mpcCommand = MagicMock()

        mpc.stop()
        mpc.mpcCommand.assert_called_with(['stop'])

if __name__ == '__main__':
    unittest.main()
