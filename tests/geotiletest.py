import unittest
from py5gmeta.common import geotile

class GeoTestCase(unittest.TestCase):

    def setUp(self):
        self.latitude = 43.295778
        self.longitude = -1.980823

    def test_get_tile_by_position(self):
        print(geotile.get_tile_by_position(self.latitude, self.longitude))

    def test_get_address(self):
        print(geotile.get_address(self.latitude, self.longitude))

    def test_get_country_from(self):
        self.assertEqual(geotile.get_country_from(self.latitude, self.longitude), 'Spain')  # add assertion here


if __name__ == '__main__':
    unittest.main()
