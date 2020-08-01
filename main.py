from src.mmag.unit_cell import Cuboid
from src.mmag.unit_cell import field_dipole, field_rectangular_box
import numpy as np

if __name__ == "__main__":
    # position = np.array([0.0, 0.0, 0.0])
    # delta = np.array([1.0, 1.0, 1.0])
    #
    # cub = Cuboid(position, delta)
    # print(cub)
    #
    # rp = np.array([.0, .0, .0], dtype=np.float64)
    # m = np.array([.0, .0, 1.0], dtype=np.float64)
    # r = np.array([.0, 1.0, 2.0], dtype=np.float64)
    # d = np.array([1.0, 1.0, 1.0], dtype=np.float64)
    #
    # dip = field_dipole(rp, m, r)
    # f = field_rectangular_box(rp, d, m, r)



    # position = np.array([1.0, 5.0, 0.0], dtype=np.float64)
    # delta = np.array([1.0, 1.0, 1.0], dtype=np.float64)
    # cub = Cuboid(position, delta)
    #
    # m = np.array([1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)], dtype=np.float64)
    # r = np.array([5.0, 5.0, 5.0], dtype=np.float64)
    #
    # dipole_field = field_dipole(cub.position, m, r)
    # box_field = cub.unit_field(r, m)
    # print(box_field, dipole_field)


    position = np.array([0.0, 0.0, 0.0], dtype=np.float64)
    m = np.array([1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)], dtype=np.float64)
    r = np.array([2.0, 3.0, 4.0], dtype=np.float64)
    dipole_field1 = field_dipole(position, m, r)

    magnitude_dipole = np.sqrt(dipole_field1.dot(dipole_field1))
    print(dipole_field1, magnitude_dipole)

    position = np.array([1.0, 1.0, 1.0], dtype=np.float64)
    m = np.array([1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)], dtype=np.float64)
    r = np.array([3.0, 4.0, 5.0], dtype=np.float64)
    dipole_field1 = field_dipole(position, m, r)

    magnitude_dipole = np.sqrt(dipole_field1.dot(dipole_field1))
    print(dipole_field1, magnitude_dipole)
