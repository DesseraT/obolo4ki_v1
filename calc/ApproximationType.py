from math import *
from sympy import *


def defineArray(N:int, deform: str):
    mas = [0] * int(sqrt(N))
    for i in range(int(sqrt(N))):
        mas[i] = [0] * int(sqrt(N))
    for i in range(int(sqrt(N))):
        for j in range(int(sqrt(N))):
            mas[i][j] = Symbol(f"{deform}[{i},{j}]")
    return mas


# hinged-fixed fastening
def hingedFixed(x, y, a, b, N:int):
    w = defineArray(N, 'w')
    u = defineArray(N, 'u')
    v = defineArray(N, 'v')
    psi_x = defineArray(N, 'psi_x')
    psi_y = defineArray(N, 'psi_y')
    W = Symbol("")
    U= Symbol("")
    V= Symbol("")
    Psi_x= Symbol("")
    Psi_y= Symbol("")
    for i in range(int(sqrt(N))):
        for j in range(int(sqrt(N))):
            w[i][j] = Symbol(f"w[{i},{j}]")
            u[i][j] = Symbol(f"u[{i},{j}]")
            v[i][j] = Symbol(f"v[{i},{j}]")
            psi_x[i][j] = Symbol(f"psi_x[{i},{j}]")
            psi_y[i][j] = Symbol(f"psi_y[{i},{j}]")

            W += w[i][j] * (sin(i * x * pi / a)) * (sin(j * y * pi / b))
            U += w[i][j] * (sin(i * x * pi / a)) * (sin(j * y * pi / b))
            V += w[i][j] * (sin(i * x * pi / a)) * (sin(j * y * pi / b))
            Psi_x = Psi_x + psi_x[i][j] * (cos(i * x * pi / a)) * (sin(j * y * pi / b))
            Psi_y = Psi_y + psi_y[i][j] * (sin(i * x * pi / a)) * (cos(j * y * pi / b))

    return W, U, V, Psi_x, Psi_y
