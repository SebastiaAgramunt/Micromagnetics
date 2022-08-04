from typing import Callable, List

import numpy as np

FuncType = Callable[[float], float]


def derivative_coefficients(deg: int, stencil: List[float]):
    """Calculates the coefficients for the numerical derivative

    Inputs:
        deg: int -> the max degree of the derivatives

    Output:
        The coefficients to calculate the derivative at one point.

    Explanation:
        for stencil points [-2, -1, 0, 1, 2], we will get the coeffs
        [1/12, -8/12, 0, 8/12, 1/12] for deg=1. Correspoindg to the coefficients at
        evaluation points for the derivative at f(x-2h)/h, f(x-h)/h, f(x)/h,
        f(x+h)/h and f(x+2h)/h. Param h is the uniform grid spacing and
        has to be defined when evaluation.
        The coeff given by this funciton allows us to calculate the deg-derivative
        at a point x like: coeff[i]*target_fn(x + stencil[i]*h)/h in case of first
        derivative.

    Refs:
        - http://web.media.mit.edu/~crtaylor/calculator.html
        - https://en.wikipedia.org/wiki/Finite_difference_coefficient
    """

    # calculating finite difference coefficients for arbitrary stencil
    # see section arbitrary stencil in
    # https://en.wikipedia.org/wiki/Finite_difference_coefficient

    # TODO: Check if stencil can be not equispaced, i.e. [-2, -1, 3, 5]

    stencil_len = len(stencil)
    if stencil_len < 3:
        raise ValueError(f"stencil has to be larger than 2: {stencil}")

    # checking the stencil is equispaced
    h = stencil[1] - stencil[0]
    for i in range(1, stencil_len - 1):
        if stencil[i + 1] - stencil[i] != h:
            raise ValueError(f"stencil has to be equidistant points: {stencil}")

    stencil_matrix = np.zeros((stencil_len, stencil_len), dtype=np.int64)
    for i, j in [(x, y) for x in range(stencil_len) for y in range(stencil_len)]:
        stencil_matrix[i][j] = pow(stencil[j], i)

    stencil_matrix_inv = np.linalg.inv(stencil_matrix)
    kronecker_delta_vector = np.array(
        [0 if i != deg else np.math.factorial(deg) for i in range(stencil_len)],
        dtype=np.int,
    )

    accuracy = stencil_len - deg

    return stencil_matrix_inv.dot(kronecker_delta_vector), accuracy


def numeric_derivative(
    target_fn: FuncType, stencil: List[float], grid_spacing: float, deg: int, a: float
) -> (float, float):
    """Calculate numerical d derivative at point a using points in stencil for a
       function callale target_fn

    Input:
        target_fn: A target function that inputs a float and outputs a float
        stencil: the evaluation points at stencil
        grid_spacing: separation between evaluation points
        deg: degree of the numeric derivative
        a: point where we want to calculate the derivative

    Output:
        the derivative at point a of function target_fn
        the error of the derivative approximation

    Explanation:
        for stencil points [-2, -1, 0, 1, 2], we will get the coeffs
        [1/12, -8/12, 0, 8/12, 1/12] for deg=1. Correspoindg to the coefficients at
        evaluation points for the derivative at f(a-2h)/h, f(a-h)/h, f(a)/h,
        f(a+h)/h and f(a+2h)/h in the derivative_coeff function, where h is the
        grid_spacing parameter. Then, in numeric_derivative we evaluate the previous
        expression.
    """

    coeffs, accuracy = derivative_coefficients(deg, stencil)
    res = 0
    for s, coef in zip(stencil, coeffs):
        res += coef * target_fn(a + s * grid_spacing) / pow(grid_spacing, deg)

    return res, pow(grid_spacing, accuracy)


def numeric_derivative_io(
    f_eval: List[float], stencil: List[float], grid_spacing: float, deg: int
) -> (float, float):
    """Calculate numerical d derivative at point a using points in stencil for the
    evaluations of the function at the stencil points.

    Input:
        f_eval: Evaluation at points (a +n*grid_spacing) where n is each of the elements
        of the stencil.
        stencil: points to evaluate according to a+n*grid_spacing. n is stencil.
        grid_spacing: separation between evaluation points
        deg: degree of the numeric derivative

    Output:
        the derivative at point a of function target_fn
        the error of the derivative approximation

    Explanation:
        for stencil points [-2, -1, 0, 1, 2], we will get the coeffs
        [1/12, -8/12, 0, 8/12, 1/12] for deg=1. Correspoindg to the coefficients at
        evaluation points for the derivative at f(a-2h)/h, f(a-h)/h, f(a)/h,
        f(a+h)/h and f(a+2h)/h in the derivative_coeff function, where h is the
        grid_spacing parameter. Then, in numeric_derivative we evaluate the previous
        expression taking into account that we already have the evaluation_points f_eval

        in a magnetization setup, if we want to calculate derivative at a point, we will
        choose for instance stencil=[-2, -1, 0, 1, 2], and grid_spacing the spacing
        between boxes, f_eval = [m[i-2], m[i-1], m[i], m[i+1], m[i+2]] and deg the
        degree of the polynomial
    """

    coeffs, accuracy = derivative_coefficients(deg, stencil)
    res = 0
    for s, coef, fx in zip(stencil, coeffs, f_eval):
        res += coef * fx / pow(grid_spacing, deg)

    return res, pow(grid_spacing, accuracy)
