from typing import List

import numpy as np

from mmag.exchange.numeric_derivatives import numeric_derivative_io

_mu0 = 1.2566370614e-6


def _m_second_derivative(
    m_xdirection: List[np.array],
    m_ydirection: List[np.array],
    m_zdirection: List[np.array],
    stencilx: List[float],
    stencily: List[float],
    stencilz: List[float],
    grid_spacing_x: float,
    grid_spacing_y: float,
    grid_spacing_z: float,
) -> np.array:
    """Calculate second derivative of m using the vector m.

    Input:
        - stencilx: stencil in the x direction
        - stencily: stencil in the y direction
        - stencilz: stencil in the z direction
        - m_xdirection: array of unit vectors of m in the x direction
        - m_ydirection: array of unit vectors of m in the y direction
        - m_zdirection: array of unit vectors of m in the z direction

    Output:
        - The vector with the second derivative of m
    """

    # check
    if (
        len(stencilx) != len(m_xdirection)
        or len(stencily) != len(m_ydirection)
        or len(stencilz) != len(m_zdirection)
    ):
        raise ValueError(
            f"stencil and m values have to be same lenght:\n{len(stencilx)}=={len(m_xdirection)}\n{len(stencily)}=={len(m_ydirection)}\n{len(stencilz)}=={len(m_zdirection)}"
        )

    if len(m_xdirection) > 2:

        m2xx, _ = numeric_derivative_io(
            [m[0] for m in m_xdirection], stencilx, grid_spacing_x, 2
        )

        m2yx, _ = numeric_derivative_io(
            [m[1] for m in m_xdirection], stencilx, grid_spacing_x, 2
        )

        m2zx, _ = numeric_derivative_io(
            [m[2] for m in m_xdirection], stencilx, grid_spacing_x, 2
        )
    else:
        m2xx, m2yx, m2zx = 0.0, 0.0, 0.0

    if len(m_ydirection) > 2:

        m2xy, _ = numeric_derivative_io(
            [m[0] for m in m_ydirection], stencily, grid_spacing_y, 2
        )

        m2yy, _ = numeric_derivative_io(
            [m[1] for m in m_ydirection], stencily, grid_spacing_y, 2
        )

        m2zy, _ = numeric_derivative_io(
            [m[2] for m in m_ydirection], stencily, grid_spacing_y, 2
        )
    else:
        m2xy, m2yy, m2zy = 0.0, 0.0, 0.0

    if len(m_zdirection) > 2:

        m2xz, _ = numeric_derivative_io(
            [m[0] for m in m_zdirection], stencilz, grid_spacing_z, 2
        )

        m2yz, _ = numeric_derivative_io(
            [m[1] for m in m_zdirection], stencilz, grid_spacing_z, 2
        )

        m2zz, _ = numeric_derivative_io(
            [m[2] for m in m_zdirection], stencilz, grid_spacing_z, 2
        )
    else:
        m2xz, m2yz, m2zz = 0.0, 0.0, 0.0

    return np.array(
        [m2xx + m2xy + m2xz, m2yx + m2yy + m2yz, m2zx + m2zy + m2zz], dtype=np.float64
    )


class Exchange:
    """Exchange object to calculate exchange field and exchange energy at a point

    Attributes:
        - grid_spacing_x: spacing in the x direction (between cells)
        - grid_spacing_y: spacing in the y direction (between cells)
        - grid_spacing_z: spacing in the z direction (between cells)
        - _A: exchange constant in J/m
        - _Ms: Saturation magnetization of the sample

    Methods:
        - exchange_field: Calculate the exchange field
        - exchange_energy_density: Calculate exchange energy per unit volume.
    """

    def __init__(
        self,
        grid_spacing_x: float,
        grid_spacing_y: float,
        grid_spacing_z: float,
        A: float = 1.3e-11,
        Ms: float = 8e5,
    ):
        self._A = A
        self._Ms = Ms

        self._grid_spacing_x = grid_spacing_x
        self._grid_spacing_y = grid_spacing_y
        self._grid_spacing_z = grid_spacing_z

    def exchange_field(
        self,
        m_xdirection: List[np.array],
        m_ydirection: List[np.array],
        m_zdirection: List[np.array],
        stencilx: List[float],
        stencily: List[float],
        stencilz: List[float],
    ) -> np.array:

        deriv2 = _m_second_derivative(
            m_xdirection,
            m_ydirection,
            m_zdirection,
            stencilx,
            stencily,
            stencilz,
            self._grid_spacing_x,
            self._grid_spacing_y,
            self._grid_spacing_z,
        )

        return 2 * self._A / (self._Ms * _mu0) * deriv2

    def exchange_energy_density(
        self,
        m_xdirection: List[np.array],
        m_ydirection: List[np.array],
        m_zdirection: List[np.array],
        stencilx: List[float],
        stencily: List[float],
        stencilz: List[float],
        m: np.array,
    ) -> float:

        he = self.exchange_field(
            m_xdirection, m_ydirection, m_zdirection, stencilx, stencily, stencilz
        )

        return -0.5 * _mu0 * self._Ms * m.dot(he)
