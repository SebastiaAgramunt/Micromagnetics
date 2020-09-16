from mmag.exchange.exchange_terms import Exchange

import numpy as np
import pytest

# TODO: implement vortex exchange energy computation
# TODO: block wall and Neel wall

# x from 0 to 1.
m_neel = lambda x: np.array(
    [np.sin(x * (np.pi)), np.cos(x * (np.pi)), 0.0], dtype=np.float64
)
m_bloch = lambda x: np.array(
    [0.0, np.cos(x * (np.pi)), np.sin(x * (np.pi))], dtype=np.float64
)
_A = 1.3e-11

testdata = [(m_neel, 5000, [0, 1], _A, _A * np.power(np.pi, 2.0)),
            (m_bloch, 5000, [0, 1], _A, _A * np.power(np.pi, 2.0))]


@pytest.mark.parametrize("m_func,mesh,rng,A,expected", testdata)
def test_exchange_energy(m_func, mesh, rng, A, expected):
    step = 1.0 / mesh
    x = np.linspace(start=step, stop=1 - step, num=mesh, endpoint=True)
    m = [m_func(a) for a in x]

    exchange = Exchange(
        grid_spacing_x=step, grid_spacing_y=step, grid_spacing_z=step, A=A, Ms=8e5
    )

    exchange_energy_density = 0.0

    stencily = []
    stencilz = []
    m_ydirection = []
    m_zdirection = []

    for i, mi in enumerate(m):
        if i<3:
            stencilx = list(range(-i, 5-i))
            m_xdirection = m[0:5]
        elif i>=3 and i<=mesh-3:
            stencilx = [-2, -1, 0, 1, 2]
            m_xdirection = m[i - 2:i + 3]
        else:
            if i == (mesh-1):
                stencilx = [-4, -3, -2, -1, 0]
                m_xdirection = m[mesh-6: mesh-1]
            elif i == (mesh-2):
                stencilx = [-3, -2, -1, 0, 1]
                m_xdirection = m[mesh - 6: mesh - 1]

        exchange_energy_density += exchange.exchange_energy_density(m_xdirection, m_ydirection, m_zdirection, stencilx, stencily, stencilz, mi)

    assert round(exchange_energy_density/mesh/_A, 2) == round(expected/_A, 2)
