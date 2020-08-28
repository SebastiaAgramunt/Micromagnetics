import pytest
import numpy as np
from mmag.exchange.numeric_derivatives import derivative_coefficients
from mmag.exchange.numeric_derivatives import numeric_derivative, numeric_derivative_io


def round_list_elements(list_to_round, digits):
    # round a list of floats to "digits" digits
    return [round(x, digits) for x in list_to_round]


# stencil, degree_derivative, accuracy, result
testdata = [
    # symmetric
    ([-1, 0, 1], 1, [-1.0 / 2.0, 0.0, 1.0 / 2.0]),
    ([-2, -1, 0, 1, 2], 1, [1.0 / 12.0, -2.0 / 3.0, 0.0, 2.0 / 3.0, -1.0 / 12.0]),
    (
        [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        5,
        [
            -13 / 288,
            19 / 36,
            -87 / 32,
            13 / 2,
            -323 / 48,
            0,
            323 / 48,
            -13 / 2,
            87 / 32,
            -19 / 36,
            13 / 288,
        ],
    ),
    (
        [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
        6,
        [
            13 / 240,
            -19 / 24,
            87 / 16,
            -39 / 2,
            323 / 8,
            -1023 / 20,
            323 / 8,
            -39 / 2,
            87 / 16,
            -19 / 24,
            13 / 240,
        ],
    ),
    # non symetric
    ([0, 1, 2, 3, 4, 5, 6], 1, [-49 / 20, 6, -15 / 2, 20 / 3, -15 / 4, 6 / 5, -1 / 6]),
    (
        [0, 1, 2, 3, 4, 5, 6, 7, 8],
        4,
        [
            1069 / 80,
            -1316 / 15,
            15289 / 60,
            -2144 / 5,
            10993 / 24,
            -4772 / 15,
            2803 / 20,
            -536 / 15,
            967 / 240,
        ],
    ),
]


@pytest.mark.parametrize("stencil,deg,expected", testdata)
def test_assert_coeffs(stencil, deg, expected):

    coeffs, accuracy = derivative_coefficients(deg, stencil)
    coeffs = round_list_elements(coeffs, 6)
    expected = round_list_elements(expected, 6)
    assert coeffs == expected


testdata = [
    # first derivative at 0
    (lambda x: np.exp(x), lambda x: np.exp(x), [-2, -1, 0, 1, 2], 0.01, 1, 0),
    (lambda x: np.cos(x), lambda x: -np.sin(x), [-2, -1, 0, 1, 2], 0.01, 1, 0),
    (
        lambda x: np.power(x, 2) + 2 * x + 1,
        lambda x: 2 * x + 2,
        [-2, -1, 0, 1, 2],
        0.01,
        1,
        0,
    ),
    (
        lambda x: np.exp(4 * x) * np.sin(3 * x),
        lambda x: np.exp(4 * x) * (4 * np.sin(3 * x) + 3 * np.cos(3 * x)),
        [-2, -1, 0, 1, 2],
        0.01,
        1,
        0,
    ),
    # second derivative at 0
    (lambda x: np.exp(x), lambda x: np.exp(x), [-2, -1, 0, 1, 2], 0.01, 2, 0),
    (lambda x: np.cos(x), lambda x: -np.cos(x), [-2, -1, 0, 1, 2], 0.01, 2, 0),
    (lambda x: np.power(x, 2) + 2 * x + 1, lambda x: 2, [-2, -1, 0, 1, 2], 0.01, 2, 0),
    (
        lambda x: np.exp(4 * x) * np.sin(3 * x),
        lambda x: np.exp(4 * x) * (7 * np.sin(3 * x) + 24 * np.cos(3 * x)),
        [-2, -1, 0, 1, 2],
        0.001,
        2,
        0,
    ),
    # second derivative at different eval points
    (lambda x: np.exp(x), lambda x: np.exp(x), [-2, -1, 0, 1, 2], 0.01, 2, 4),
    (lambda x: np.cos(x), lambda x: -np.cos(x), [-2, -1, 0, 1, 2], 0.01, 2, 2),
    (lambda x: np.power(x, 2) + 2 * x + 1, lambda x: 2, [-2, -1, 0, 1, 2], 0.01, 2, 5),
    (
        lambda x: np.exp(4 * x) * np.sin(3 * x),
        lambda x: np.exp(4 * x) * (7 * np.sin(3 * x) + 24 * np.cos(3 * x)),
        [-2, -1, 0, 1, 2],
        0.001,
        2,
        1,
    ),
    # second derivative at different eval points other stencils
    (lambda x: np.exp(x), lambda x: np.exp(x), [-2, -1, 0, 1, 2, 3], 0.01, 2, 4),
    (lambda x: np.cos(x), lambda x: -np.cos(x), [-1, 0, 1, 2, 3], 0.01, 2, 2),
    (lambda x: np.power(x, 2) + 2 * x + 1, lambda x: 2, [0, 1, 2, 3, 4], 0.01, 2, 5),
    (
        lambda x: np.exp(4 * x) * np.sin(3 * x),
        lambda x: np.exp(4 * x) * (7 * np.sin(3 * x) + 24 * np.cos(3 * x)),
        [-5, -4, -3, -2, -1, 0],
        0.001,
        2,
        1,
    ),
]


@pytest.mark.parametrize(
    "target_fn, derivative_fn, stencil,grid_spacing,deg,a", testdata
)
def test_assert_derivative_function(
    target_fn, derivative_fn, stencil, grid_spacing, deg, a
):
    res, _ = numeric_derivative(target_fn, stencil, grid_spacing, deg, a)
    expected = derivative_fn(a)

    res = round(res, 6)
    expected = round(expected, 6)

    assert res == expected


@pytest.mark.parametrize(
    "target_fn, derivative_fn, stencil,grid_spacing,deg,a", testdata
)
def test_assert_derivative_with_eval(
    target_fn, derivative_fn, stencil, grid_spacing, deg, a
):

    f_eval = [target_fn(a + n * grid_spacing) for n in stencil]
    res, _ = numeric_derivative_io(f_eval, stencil, grid_spacing, deg)

    expected = derivative_fn(a)
    res = round(res, 6)
    expected = round(expected, 6)

    assert res == expected
