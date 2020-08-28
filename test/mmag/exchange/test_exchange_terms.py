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

testdata = [(m_neel, 1000, [0, 1], _A, _A * np.power(np.pi, 2.0))]


@pytest.mark.parametrize("m_func,mesh,rng,A,expected", testdata)
def test_exchange_energy(m_func, mesh, rng, A, expected):
    step = 1.0 / mesh
    x = np.linspace(start=step, stop=1 - step, num=mesh, endpoint=True)
    m = [m_func(a) for a in x]

    exchange = Exchange(
        grid_spacing_x=step, grid_spacing_y=step, grid_spacing_z=step, A=A, Ms=8e5
    )

    print(m)

    assert True == False
