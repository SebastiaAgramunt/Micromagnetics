import unittest

import numpy as np

from mmag.unit_cell.cell import Cuboid
from mmag.unit_cell.fields import field_dipole

_acc = 0.0001

# Following tests compare the magnetic field created by a dipole to the field generated by the uniformly
# charged sheets. If far enough, the resulting fields must be similar
class TestCubicCell(unittest.TestCase):
    def setUp(self):
        position = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        delta = np.array([1.0, 1.0, 1.0], dtype=np.float64)
        self.init_obj = Cuboid(position, delta)

    def test_magnetic_field_1(self):
        # Testing field unirormly magnetized in Z

        m = np.array([0.0, 0.0, 1.0], dtype=np.float64)
        r = np.array([0.0, 0.0, 3.0], dtype=np.float64)

        dipole_field = field_dipole(self.init_obj.position, m, r)
        box_field = self.init_obj.unit_field(r, m)

        magnitude_dipole = np.sqrt(dipole_field.dot(dipole_field))
        magnitude_box = np.sqrt(box_field.dot(box_field))

        self.assertTrue(np.fabs(magnitude_box - magnitude_dipole) < _acc)
        self.assertTrue(np.fabs(dipole_field[0] - box_field[0]) < _acc)
        self.assertTrue(np.fabs(dipole_field[1] - box_field[1]) < _acc)
        self.assertTrue(np.fabs(dipole_field[2] - box_field[2]) < _acc)

    def test_magnetic_field_2(self):
        # Testing uniform magnetized in X is same as uniformly magnetized in Z
        m = np.array([0.0, 0.0, 1.0], dtype=np.float64)
        r = np.array([0.0, 0.0, 3.0], dtype=np.float64)

        box_field_1 = self.init_obj.unit_field(r, m)

        m = np.array([1.0, 0.0, 0.0], dtype=np.float64)
        r = np.array([3.0, 0.0, 0.0], dtype=np.float64)

        box_field_2 = self.init_obj.unit_field(r, m)
        self.assertTrue(np.fabs(box_field_1[2] - box_field_2[0]) < _acc)

    def test_magnetic_field_3(self):
        # Testing at different positions
        m = np.array([0.0, 0.0, 1.0], dtype=np.float64)
        r = np.array([4.0, 1.0, 2.0], dtype=np.float64)

        dipole_field = field_dipole(self.init_obj.position, m, r)
        box_field = self.init_obj.unit_field(r, m)

        magnitude_dipole = np.sqrt(dipole_field.dot(dipole_field))
        magnitude_box = np.sqrt(box_field.dot(box_field))

        self.assertTrue(np.fabs(magnitude_box - magnitude_dipole) < _acc)
        self.assertTrue(np.fabs(dipole_field[0] - box_field[0]) < _acc)
        self.assertTrue(np.fabs(dipole_field[1] - box_field[1]) < _acc)
        self.assertTrue(np.fabs(dipole_field[2] - box_field[2]) < _acc)

    def test_magnetic_field_4(self):
        m = np.array([0.0, 0.0, 1.0], dtype=np.float64)
        r = np.array([1.0, 3.0, 2.0], dtype=np.float64)

        dipole_field = field_dipole(self.init_obj.position, m, r)
        box_field = self.init_obj.unit_field(r, m)

        magnitude_dipole = np.sqrt(dipole_field.dot(dipole_field))
        magnitude_box = np.sqrt(box_field.dot(box_field))

        self.assertTrue(np.fabs(magnitude_box - magnitude_dipole) < _acc)
        self.assertTrue(np.fabs(dipole_field[0] - box_field[0]) < _acc)
        self.assertTrue(np.fabs(dipole_field[1] - box_field[1]) < _acc)
        self.assertTrue(np.fabs(dipole_field[2] - box_field[2]) < _acc)


class TestCubicCellDifferentDirections(unittest.TestCase):
    def setUp(self):
        position = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        delta = np.array([1.0, 1.0, 1.0], dtype=np.float64)
        self.init_obj = Cuboid(position, delta)

    def test_magnetic_field_1(self):
        # Testing field unirormly magnetized in Z

        m = np.array(
            [1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)],
            dtype=np.float64,
        )
        r = np.array([0.0, 0.0, 3.0], dtype=np.float64)

        dipole_field = field_dipole(self.init_obj.position, m, r)
        box_field = self.init_obj.unit_field(r, m)

        magnitude_dipole = np.sqrt(dipole_field.dot(dipole_field))
        magnitude_box = np.sqrt(box_field.dot(box_field))

        self.assertTrue(np.fabs(magnitude_box - magnitude_dipole) < _acc)
        self.assertTrue(np.fabs(dipole_field[0] - box_field[0]) < _acc)
        self.assertTrue(np.fabs(dipole_field[1] - box_field[1]) < _acc)
        self.assertTrue(np.fabs(dipole_field[2] - box_field[2]) < _acc)

    def test_magnetic_field_2(self):
        # Testing field unirormly magnetized in Z

        m = np.array(
            [1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)],
            dtype=np.float64,
        )
        r = np.array([1.0, 0.0, 2.0], dtype=np.float64)

        dipole_field = field_dipole(self.init_obj.position, m, r)
        box_field = self.init_obj.unit_field(r, m)

        magnitude_dipole = np.sqrt(dipole_field.dot(dipole_field))
        magnitude_box = np.sqrt(box_field.dot(box_field))

        self.assertTrue(np.fabs(magnitude_box - magnitude_dipole) < _acc)
        self.assertTrue(np.fabs(dipole_field[0] - box_field[0]) < _acc)
        self.assertTrue(np.fabs(dipole_field[1] - box_field[1]) < _acc)
        self.assertTrue(np.fabs(dipole_field[2] - box_field[2]) < _acc)

    def test_magnetic_field_3(self):
        # Testing field uniformly magnetized in Z

        m = np.array(
            [1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)],
            dtype=np.float64,
        )
        r = np.array([1.0, 5.0, 2.0], dtype=np.float64)

        dipole_field = field_dipole(self.init_obj.position, m, r)
        box_field = self.init_obj.unit_field(r, m)

        magnitude_dipole = np.sqrt(dipole_field.dot(dipole_field))
        magnitude_box = np.sqrt(box_field.dot(box_field))

        self.assertTrue(np.fabs(magnitude_box - magnitude_dipole) < _acc)
        self.assertTrue(np.fabs(dipole_field[0] - box_field[0]) < _acc)
        self.assertTrue(np.fabs(dipole_field[1] - box_field[1]) < _acc)
        self.assertTrue(np.fabs(dipole_field[2] - box_field[2]) < _acc)


class TestCubicCellNotOrigin(unittest.TestCase):
    def setUp(self):
        position = np.array([1.0, 2.0, 3.0], dtype=np.float64)
        delta = np.array([1.0, 1.0, 1.0], dtype=np.float64)
        self.init_obj = Cuboid(position, delta)

    def test_magnetic_field_1(self):
        # Testing field unirormly magnetized in Z

        m = np.array(
            [1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)],
            dtype=np.float64,
        )
        r = np.array([7.0, 8.0, 7.0], dtype=np.float64)

        dipole_field = field_dipole(self.init_obj.position, m, r)
        box_field = self.init_obj.unit_field(r, m)

        magnitude_dipole = np.sqrt(dipole_field.dot(dipole_field))
        magnitude_box = np.sqrt(box_field.dot(box_field))

        print(magnitude_box, magnitude_dipole)
        print(box_field, dipole_field)

        self.assertTrue(np.fabs(magnitude_box - magnitude_dipole) < _acc)
        self.assertTrue(np.fabs(dipole_field[0] - box_field[0]) < _acc)
        self.assertTrue(np.fabs(dipole_field[1] - box_field[1]) < _acc)
        self.assertTrue(np.fabs(dipole_field[2] - box_field[2]) < _acc)


if __name__ == "__main__":
    unittest.main()
