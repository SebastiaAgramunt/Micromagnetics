from src import Cuboid
from src import field_dipole, field_rectangular_box
import numpy as np

if __name__ == "__main__":
    position = np.array([0.0, 0.0, 0.0])
    delta = np.array([1.0, 1.0, 1.0])

    cub = Cuboid(position, delta)
    print(cub)

    rp = np.array([.0, .0, .0], dtype=np.float64)
    m = np.array([.0, .0, 1.0], dtype=np.float64)
    r = np.array([.0, 1.0, 2.0], dtype=np.float64)
    d = np.array([1.0, 1.0, 1.0], dtype=np.float64)

    dip = field_dipole(rp, m, r)
    f = field_rectangular_box(rp, d, m, r)
