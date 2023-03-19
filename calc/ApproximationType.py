from math import *
from sympy import *


def defineArray(N: int, deform: str):
    mas = [0] * int(sqrt(N))
    for i in range(int(sqrt(N))):
        mas[i] = [0] * int(sqrt(N))
    for i in range(int(sqrt(N))):
        for j in range(int(sqrt(N))):
            mas[i][j] = Symbol(f"{deform}[{i},{j}]")
    return mas


class Fastening:

    def __init__(self, a, b, N: int, fasteningType:str, shellSymmetry:str):
        self.x, self.y = symbols('x y')
        self.a = a
        self.b = b
        self.N = N
        self.shellSymmetry = shellSymmetry
        self.W = Symbol("")
        self.U = Symbol("")
        self.V = Symbol("")
        self.Psi_x = Symbol("")
        self.Psi_y = Symbol("")
        if fasteningType == "hinged-fixed":
            self.hingedFixed()
        elif fasteningType == "strict":
            self.strict()

    def hingedFixed(self):
        w = defineArray(self.N, 'w')
        u = defineArray(self.N, 'u')
        v = defineArray(self.N, 'v')
        psi_x = defineArray(self.N, 'psi_x')
        psi_y = defineArray(self.N, 'psi_y')
        for i in range(int(sqrt(self.N))):
            for j in range(int(sqrt(self.N))):
                w[i][j] = Symbol(f"w[{i},{j}]")
                u[i][j] = Symbol(f"u[{i},{j}]")
                v[i][j] = Symbol(f"v[{i},{j}]")
                psi_x[i][j] = Symbol(f"psi_x[{i},{j}]")
                psi_y[i][j] = Symbol(f"psi_y[{i},{j}]")
                if self.shellSymmetry == "symmetry":
                    self.W += w[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.U += u[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.V += v[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_x += psi_x[i][j] * (cos(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_y += psi_y[i][j] * (sin(i * self.x * pi / self.a)) * (cos(j * self.y * pi / self.b))
                elif self.shellSymmetry == "xAsymmetry":
                    self.W += w[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.U += u[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.V += v[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_x += psi_x[i][j] * (cos(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_y += psi_y[i][j] * (sin(i * self.x * pi / self.a)) * (cos(j * self.y * pi / self.b))
                elif self.shellSymmetry == "yAsymmetry":
                    self.W += w[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.U += u[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.V += v[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_x += psi_x[i][j] * (cos(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_y += psi_y[i][j] * (sin(i * self.x * pi / self.a)) * (cos(j * self.y * pi / self.b))

    def strict(self):
        w = defineArray(self.N, 'w')
        u = defineArray(self.N, 'u')
        v = defineArray(self.N, 'v')
        psi_x = defineArray(self.N, 'psi_x')
        psi_y = defineArray(self.N, 'psi_y')
        for i in range(int(sqrt(self.N))):
            for j in range(int(sqrt(self.N))):
                w[i][j] = Symbol(f"w[{i},{j}]")
                u[i][j] = Symbol(f"u[{i},{j}]")
                v[i][j] = Symbol(f"v[{i},{j}]")
                psi_x[i][j] = Symbol(f"psi_x[{i},{j}]")
                psi_y[i][j] = Symbol(f"psi_y[{i},{j}]")
                if (self.shellSymmetry == "symmetry"):
                    self.W += w[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.U += u[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.V += v[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_x += psi_x[i][j] * (cos(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_y += psi_y[i][j] * (sin(i * self.x * pi / self.a)) * (cos(j * self.y * pi / self.b))
                elif (self.shellSymmetry == "xAsymmetry"):
                    self.W += w[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.U += u[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.V += v[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_x += psi_x[i][j] * (cos(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_y += psi_y[i][j] * (sin(i * self.x * pi / self.a)) * (cos(j * self.y * pi / self.b))
                elif (self.shellSymmetry == "yAsymmetry"):
                    self.W += w[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.U += u[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.V += v[i][j] * (sin(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_x += psi_x[i][j] * (cos(i * self.x * pi / self.a)) * (sin(j * self.y * pi / self.b))
                    self.Psi_y += psi_y[i][j] * (sin(i * self.x * pi / self.a)) * (cos(j * self.y * pi / self.b))
