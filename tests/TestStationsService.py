import unittest
from unittest.mock import MagicMock

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from stations_service import StationsServiceFactory

class TestStationsService(unittest.TestCase):
    def test_if_service_is_singleton(self):
        first = StationsServiceFactory.getService()
        second = StationsServiceFactory.getService()

        first.currentIndex = 10

        self.assertEqual(first.currentIndex, second.currentIndex)

    def test_if_service_returns_stations_list(self):
        service = StationsServiceFactory.getService()
        self.assertTrue(service.getStations())
