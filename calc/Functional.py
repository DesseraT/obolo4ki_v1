from sympy import *


def calculateFunctional(x, y, a, b, q, A, B, W, U, V, N_x, N_y, N_xy, N_yx,M_x, M_y, M_xy, M_yx, eps_x, eps_y, Gamma_xy, Q_x, Q_y, P_x, P_y, Xi_1, Xi_2, Xi_12, Thetta_1, Thetta_2, psi_x, psi_y  ):
    Es = 1 / 2 * integrate(integrate(
        A * B * (N_x * eps_x + N_y * eps_y + 1 / 2 * (N_xy + N_yx) * Gamma_xy + M_x * Xi_1 + M_y * Xi_2 + (M_xy + M_yx) * Xi_12 + Q_x * (psi_x - Thetta_1) + Q_y * (psi_y - Thetta_2) -2*(q*W + P_x*U + P_y*V))
    ,(x, 0, a))
    ,(y, 0, b))
    return Es
