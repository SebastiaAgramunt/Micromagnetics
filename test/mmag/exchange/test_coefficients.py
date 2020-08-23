import pytest
from mmag.exchange.coefficients import derivative_coefficients

from typing import List

def round_list_elements(list_to_round, digits):
    # round a list of floats to "digits" digits
    return [round(x, digits) for x in list_to_round]

# stencil, degree_derivative, accuracy, result
testdata = [
	# symmetric
    ([-1, 0, 1], 1, 2, [-1.0/2.0, 0.0, 1.0/2.0]),
    ([-2, -1, 0, 1, 2], 1, 4, [1.0/12.0, -2.0/3.0, 0.0, 2.0/3.0, -1.0/12.0]),
    ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 5, 6, [-13/288, 19/36, -87/32, 13/2, -323/48, 0, 323/48, -13/2, 87/32, -19/36, 13/288]),
    # non symetric
    ([0, 1, 2, 3, 4, 5, 6], 1, 6, [-49/20, 6, -15/2, 20/3, -15/4, 6/5, -1/6]),
]

@pytest.mark.parametrize("stencil,deg,accuracy,expected", testdata)
def test_assert_coeffs(stencil, deg, accuracy, expected):

    coeffs = round_list_elements(derivative_coefficients(deg, stencil), 6)
    expected = round_list_elements(expected, 6)
    assert coeffs==expected



