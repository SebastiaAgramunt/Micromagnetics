import numpy as np


def _epsilon(i, j, k):
    """
    Levi-Civita tensor
    """
    assert i>=0 and i<3, "Index i goes from 0 to 2 included"
    assert j>=0 and j<3, "Index j goes from 0 to 2 included"
    assert k>=0 and k<3, "Index k goes from 0 to 2 included"
    
    if (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        return +1
    if (i, j, k) in [(2, 1, 0), (0, 2, 1), (1, 0, 2)]:
        return -1
    return 0

def _delta(i, j):
    assert i!=0 or i!=1, "i index can only be 0 or 1"
    assert j!=0 or j!=1, "j index can only be 0 or 1"
    
    if i==j:
        return 1
    return 0

def RotationMatrix(angle: float, axis: np.array=np.array([0.0, 0.0, 1.0], dtype=np.float64)):
    """
    Given a unitary axis vector in 3D perform a rotation of a certain angle.
    """
    assert axis.dot(axis) < 1.0 + 0.0001, "axis has to be unitary vector"
    assert axis.dot(axis) > 1.0 - 0.0001, "axis has to be unitary vector"
    
    p1, p2, p3 = axis[0], axis[1], axis[2]
    
    R = np.zeros((3,3), dtype=np.float64)
    for i in range(3):
        for j in range(3):
            R[i][j] = np.cos(angle)*_delta(i,j) + (1 - np.cos(angle))*axis[i]*axis[j]
            for k in range(3):
                R[i][j] -= np.sin(angle)*_epsilon(i, j, k)*axis[k]
            
    return R