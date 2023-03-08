from math import *
from sympy import *
from calc.Geometrical import *
class Physical:
    def __init__(self,geom: Geometrical, E1, E2, mu12, mu21, G12, G13, G23):
        self.E1      = E1   
        self.E2      = E2   
        self.mu12    = mu12 
        self.mu21    = mu21 
        self.G12     = G12  
        self.G13     = G13  
        self.G23     = G23
        self.geom : Geometrical = geom
        self.tau()
        self.sigma()
    def __f(self):
        return 6 * (1 / 4 - self.geom.z ** 2 / self.geom.h ** 2)
    def sigma(self):
        self.Sigma_X = Symbol("")
        self.Sigma_Y = Symbol("")
        self.Sigma_I = Symbol("")
        self.Sigma_X = self.E1 / (1-self.mu12*self.mu21) * (self.geom.Eps_Y + self.mu21*self.geom.Eps_Y + self.geom.z*(self.geom.Xi_1 + self.mu21*self.geom.Xi_2))
        self.Sigma_Y = self.E2 / (1-self.mu21*self.mu12) * (self.geom.Eps_X + self.mu12*self.geom.Eps_X + self.geom.z*(self.geom.Xi_2 + self.mu12*self.geom.Xi_1))
        self.Sigma_I = self.Sigma_X ** 2 + self.Sigma_Y ** 2 - self.Sigma_Y*self.Sigma_X + 3*(self.tau_XY ** 2 + self.tau_XZ ** 2 + self.tau_YZ ** 2) 
    def tau(self):
        self.tau_XY = Symbol("")
        self.tau_XZ = Symbol("")
        self.tau_YZ = Symbol("")
        self.tau_XY = self.G12 * (self.geom.Gamma_XY + 2 * self.geom.z * self.geom.Xi_12)
        self.tau_XZ = self.G13 * self.geom.k * self.__f() * (self.geom.Psi_X - self.geom.Thetta_1)
        self.tau_YZ = self.G23 * self.geom.k * self.__f() * (self.geom.Psi_Y - self.geom.Thetta_2)

