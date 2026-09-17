import unittest
from src.api_data import opt_offset
from src.surf_spot_class import Direction

class TestApiData(unittest.TestCase):

    def test_opt_offset(self):
        direction = Direction.E.value
        direction2 = Direction.NE.value #45
        data = int(292.234565)
        data2 = int(345.23)
        result = opt_offset(data, direction)
        result2 = opt_offset(data2, direction2)
        self.assertEqual(22, result)
        self.assertEqual(120, result2)

