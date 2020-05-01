import numpy as np

def field_dipole(rp: np.array, m: np.array, r: np.array):
    """

    :param rp: position of the dipole
    :param m: magnetization of the dipole
    :param r: postion to calculate the field
    :return: vector field
    """
    r_ = r-rp

    m_ = 3.0*r*m.dot(r_)/np.power(r_.dot(r_), 5.0/2.0) - m/np.power(r_.dot(r_), 3.0/2.0)
    return m_/(4.0*np.pi)


def field_rectangular_box(rp: np.array, d: np.array, m: np.array, r: np.array):

    I = _interaction_matrix(rp, d, r)
    return I.dot(m)


def _interaction_matrix(rp: np.array, d: np.array, r: np.array):
    x_c, y_c, z_c = rp
    dx, dy, dz = d
    x, y, z = r

    nxx = _hxx(x_c, y_c, z_c, dx, dy, dz, x, y, z)
    nyy = _hyy(x_c, y_c, z_c, dx, dy, dz, x, y, z)
    nzz = _hzz(x_c, y_c, z_c, dx, dy, dz, x, y, z)

    nxy = _hxy(x_c, y_c, z_c, dx, dy, dz, x, y, z)
    nxz = _hxz(x_c, y_c, z_c, dx, dy, dz, x, y, z)
    nyz = _hyz(x_c, y_c, z_c, dx, dy, dz, x, y, z)

    # interaction matrix
    I = np.array([[nxx, nxy, nxz], [nxy, nyy, nyz], [nxz, nyz, nzz]])

    return I


_coefs = [(1, 0, 0), (0, 1, 0),
          (0, 0, 1), (1, 1, 0),
          (1, 0, 1), (0, 1, 1),
          (1, 1, 1), (0, 0, 0)]

def _hzz(x_c: np.float64, y_c:np.float64, z_c: np.float64, dx: np.float64, dy: np.float64, dz: np.float64,
         x: np.float64, y: np.float64, z: np.float64):
    '''
    :param x_c: X position of the cell
    :param y_c: Y position of the cell
    :param z_c: Z position of the cell
    :param dx: Length of cell in direction X
    :param dy: Length of cell in direction Y
    :param dz: Length of cell in direction Z
    :param x: X position where to calculate field
    :param y: Y position where to calculate field
    :param z: Z position where to calculate field
    :return:
    The z field component at x, y, z due to a cell with center x_c, y_c, z_c uniformly magnetized
    in the positive z direction.
    '''

    f = np.float64(0.0)
    for alpha, beta, gamma in _coefs:
        ddx, ddy, ddz = int(pow(-1, alpha - 1)), int(pow(-1, beta - 1)), int(pow(-1, gamma - 1))
        sx, sy, sz = x_c + ddx * dx / 2.0, y_c + ddy * dy / 2.0, z_c + ddz * dz / 2.0

        d = np.sqrt(np.power(x - sx, 2.0) + np.power(y - sy, 2.0) + np.power(z - sz, 2.0))
        arg = (x - sx) * (y - sy) / ((z - sz) * d)

        f += int(pow(-1, alpha + beta + gamma + 1)) * np.arctan(arg)

    return f / (4.0 * np.pi)


def _hxx(x_c: np.float64, y_c: np.float64, z_c: np.float64, dx: np.float64, dy: np.float64, dz: np.float64,
         x: np.float64, y: np.float64, z: np.float64):
    # Calculates the  x field component at x, y, z due to a cell with center x_c, y_c, z_c uniformly magnetized
    # in the positive x direction.
    return _hzz(z_c, y_c, x_c, dz, dy, dx, z, y, x)


def _hyy(x_c: np.float64, y_c: np.float64, z_c: np.float64, dx: np.float64, dy: np.float64, dz: np.float64,
         x: np.float64, y: np.float64, z: np.float64):
    # Calculates the y field component at x, y, z due to a cell with center x_c, y_c, z_c uniformly magnetized
    # in the positive y direction.
    return _hzz(x_c, z_c, y_c, dx, dz, dy, x, z, y)


def _hxz(x_c: np.float64, y_c: np.float64, z_c: np.float64, dx: np.float64, dy: np.float64, dz: np.float64,
         x: np.float64, y: np.float64, z: np.float64):
    '''
    :param x_c: X position of the cell
    :param y_c: Y position of the cell
    :param z_c: Z position of the cell
    :param dx: Length of cell in direction X
    :param dy: Length of cell in direction Y
    :param dz: Length of cell in direction Z
    :param x: X position where to calculate field
    :param y: Y position where to calculate field
    :param z: Z position where to calculate field
    :return:
    The x component of the field due to a uniformly magnetized cell along z direction.
    '''
    f = np.float64(0.0)
    for alpha, beta, gamma in _coefs:
        ddx, ddy, ddz = int(pow(-1, alpha - 1)), int(pow(-1, beta - 1)), int(pow(-1, gamma - 1))
        sx, sy, sz = x_c + ddx * dx / 2.0, y_c + ddy * dy / 2.0, z_c + ddz * dz / 2.0

        d = np.sqrt(np.power(x - sx, 2.0) + np.power(y - sy, 2.0) + np.power(z - sz, 2.0))
        arg = np.log(np.fabs(y - sy + d))

        cont = int(pow(-1, alpha + beta + gamma + 1)) * arg

        f += cont

    return -f / (4.0 * np.pi)


def _hxy(x_c: np.float64, y_c: np.float64, z_c: np.float64, dx: np.float64, dy: np.float64, dz: np.float64,
         x: np.float64, y: np.float64, z: np.float64):
    return _hxz(x_c, z_c, y_c, dx, dz, dy, x, z, y)


def _hyz(x_c: np.float64, y_c: np.float64, z_c: np.float64, dx: np.float64, dy: np.float64, dz: np.float64,
         x: np.float64, y: np.float64, z: np.float64):
    return _hxz(y_c, x_c, z_c, dy, dx, dz, y, x, z)