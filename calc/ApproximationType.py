import math
from sympy import *


def defineArray(N:int):
    mas = [0] * int(math.sqrt(N))
    for i in range(math.sqrt(N)):
        mas[i] = [0] * math.sqrt(N)
    return mas


# hinged-fixed fastening
def hingedFixed(x, y, a, b, N:int):
    w = defineArray(N)
    u = defineArray(N)
    v = defineArray(N)
    psi_x = defineArray(N)
    psi_y = defineArray(N)
    W, U, V, Psi_x, Psi_y = 0

    for i in range(1, math.sqrt(N)):
        for j in range(1, math.sqrt(N)):
            w[i][j] = symbols(f"w[{i},{j}]")
            u[i][j] = symbols(f"u[{i},{j}]")
            v[i][j] = symbols(f"v[{i},{j}]")
            psi_x[i][j] = symbols(f"psi_x[{i},{j}]")
            psi_y[i][j] = symbols(f"psi_y[{i},{j}]")

            W = W + w[i][j] * (sin(i * x * math.pi / a)) * (sin(j * y * math.pi / b))
            U = U + w[i][j] * (sin(i * x * math.pi / a)) * (sin(j * y * math.pi / b))
            V = V + w[i][j] * (sin(i * x * math.pi / a)) * (sin(j * y * math.pi / b))
            Psi_x = Psi_x + psi_x[i][j] * (cos(i * x * math.pi / a)) * (sin(j * y * math.pi / b))
            Psi_y = Psi_y + psi_y[i][j] * (sin(i * x * math.pi / a)) * (cos(j * y * math.pi / b))

    return W, U, V, Psi_x, Psi_y
