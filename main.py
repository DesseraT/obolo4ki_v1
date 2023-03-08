# imports
from calc.NewtonMethod import NewtonMethod
from sympy import *
from calc.ApproximationType import *
from calc.Geometrical import *
# INPUT DATA
N = 16

h = 0.00022
a = 0.2
b = 0.2

angle = 0

mu = 0.123
mu12 = mu
mu21 = mu

# theta = 0.2618
R_1 = 7.273
R_2 = 7.273

# E = 2.1*10**5
E_1 = 2.1 * 10 ** 5
E_2 = 2.1 * 10 ** 5

eps = 0.05

F_1_pos = 508
F_1_neg = -209
F_2_pos = 246
F_2_neg = -117

a_1 = 0
q0 = 0.33

F_12 = 43
F_12_pos_45 = 130
F_12_neg_45 = 130

p = 1800

k = 5 / 6


A = 1
B = 1
P_x = 0
P_y = 0
k_x = 1 / R_1
k_y = 1 / R_2

# define symbol variables
x, y = symbols('x y')

W, U, V, Psi_x, Psi_y = hingedFixed(x, y, a, b, N)
Phys = Physical(W,U,V,Psi_x, Psi_y, A,B,k_x,k_y, k,h)
print(Phys.Gamma_XY)
#123