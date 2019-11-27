import unittest
import oyaml as yaml

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from stations_parser import StationsParser

class TestStationsParser(unittest.TestCase):
    def test_returns_stations_from_yaml(self):
        data = '"[EN] BBC World News": "http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-einws"\n"[EN] BBC Radio 1": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p"\n"[EN] BBC Radio 2": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p"'

        stationsParser = StationsParser()
        results = stationsParser.getStationsFromYaml(
            yaml.load(data, Loader=yaml.Loader)
        )

        self.assertEqual(results[0].get('name'), "[EN] BBC World News")
        self.assertEqual(results[0].get('url'), "http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-einws")

        self.assertEqual(results[1].get('name'), "[EN] BBC Radio 1")
        self.assertEqual(results[1].get('url'), "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p")

        self.assertEqual(results[2].get('name'), "[EN] BBC Radio 2")
        self.assertEqual(results[2].get('url'), "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p")

if __name__ == '__main__':
    unittest.main()
