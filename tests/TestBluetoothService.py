import unittest
from unittest.mock import MagicMock

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from bluetooth_service import BluetoothServiceFactory

class TestBluetoothService(unittest.TestCase):
    def test_if_service_is_singleton(self):
        first = BluetoothServiceFactory.getService()
        second = BluetoothServiceFactory.getService()

        first.bluetoothSpeakerDevice = "test_device"

        self.assertEqual(first.bluetoothSpeakerDevice, second.bluetoothSpeakerDevice)
