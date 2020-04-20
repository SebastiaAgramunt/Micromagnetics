from mmag.unit_cell.cell import Cuboid
import numpy as np

if __name__ == "__main__":
    position = np.array([0.0, 0.0, 0.0])
    delta = np.array([1.0, 1.0, 1.0])

    cub = Cuboid(position, delta)
    print(cub)