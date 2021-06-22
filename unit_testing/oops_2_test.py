import unittest
from dataclasses import FrozenInstanceError

from concepts.oops_2 import GeoPosition


class GeoPositionTests(unittest.TestCase):

    def test_invalid_geo_position(self):
        with self.assertRaises(ValueError):
            GeoPosition(None, None)
        with self.assertRaises(ValueError):
            GeoPosition(10, None)
        with self.assertRaises(ValueError):
            GeoPosition(None, 10)
        with self.assertRaises(ValueError):
            GeoPosition(180, 10)
        with self.assertRaises(ValueError):
            GeoPosition(10, 270)
        with self.assertRaises(ValueError):
            GeoPosition(180, 270)

    def test_valid_geo_position(self):
        india = GeoPosition(20.5937, 78.9629)
        self.assertTrue(india)
        self.assertIsInstance(india, GeoPosition)

    def test_geo_position_direction(self):
        india = GeoPosition(20.5937, 78.9629)
        self.assertEqual(repr(india), "GeoPosition(Latitude=20.5937° N,Longitude=78.9629° E)")
        self.assertEqual(f"{india!r}", "GeoPosition(Latitude=20.5937° N,Longitude=78.9629° E)")
        self.assertEqual(str(india), "(Latitude=20.5937° N,Longitude=78.9629° E)")
        self.assertEqual(f"{india!s}", "(Latitude=20.5937° N,Longitude=78.9629° E)")
        self.assertEqual(format(india), "(Latitude=20.59° N,Longitude=78.96° E)")
        self.assertEqual(format(india, ".1"), "(Latitude=20.6° N,Longitude=79.0° E)")
        self.assertEqual(format(india, ".3"), "(Latitude=20.594° N,Longitude=78.963° E)")

    def test_geo_position_immutability(self):
        india = GeoPosition(20.5937, 78.9629)
        self.assertIsInstance(india, GeoPosition)
        with self.assertRaises(FrozenInstanceError):
            india.latitude = 10.0
        with self.assertRaises(FrozenInstanceError):
            india.longitude = 10.0

    def test_geo_position_collections(self):
        india = GeoPosition(20.5937, 78.9629)
        england = GeoPosition(55.3781, 3.4360)
        country_gps_seq = (india, england)
        print(type(country_gps_seq))
        self.assertIsInstance(country_gps_seq, tuple)
        country_gps_list = [india, england]
        self.assertIsInstance(country_gps_list, list)
        self.assertListEqual(sorted(country_gps_list), sorted([india, england]))
        country_gps_set = {india, england, england, england, india}
        self.assertIsInstance(country_gps_set, set)
        self.assertCountEqual(country_gps_set, [india, england])
        country_gps_dict = {"india": india, "england": england, "india": india, "england": england}
        self.assertIsInstance(country_gps_dict, dict)
        self.assertCountEqual(country_gps_dict, {"india": india, "england": england})

    if __name__ == '__main__':
        unittest.main()
