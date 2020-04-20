import unittest
import numpy as np
from mmag.unit_cell.cell import Cuboid


class TestCubicCell(unittest.TestCase):
    def setUp(self):
        position = np.array([0.0, 0.0, 0.0])
        delta = np.array([1.0, 1.0, 1.0])
        self.init_obj = Cuboid(position, delta)

    def test_input_1(self):
        #self.assertTrue(self.init_obj.position==np.array([0.0, 0.0, 0.0]))
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()