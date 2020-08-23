import numpy as np
from typing import List

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
    # see section arbitrary stencil in https://en.wikipedia.org/wiki/Finite_difference_coefficient

    # TODO: Check if stencil can be not equispaced, i.e. [-2, -1, 3, 5]

    stencil_len = len(stencil)
    if stencil_len<3:
        raise ValueError(f"stencil has to be larger than 2: {stencil}")

    # checking the stencil is equispaced
    h = stencil[1] - stencil[0]
    for i in range(1, stencil_len-1):
        if stencil[i+1] - stencil[i] != h:
            raise ValueError(f"stencil has to be equidistant points: {stencil}")
    
    stencil_matrix = np.zeros((stencil_len, stencil_len), dtype=np.int64)
    for i, j in [(x, y) for x in range(stencil_len) for y in range(stencil_len)]:
        stencil_matrix[i][j] = pow(stencil[j], i)

    stencil_matrix_inv = np.linalg.inv(stencil_matrix)
    kronecker_delta_vector = np.array(
        [0 if i != deg else np.math.factorial(deg) for i in range(stencil_len)],
        dtype=np.int,
    )

    return stencil_matrix_inv.dot(kronecker_delta_vector)


