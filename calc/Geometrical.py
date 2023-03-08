from math import *
from sympy import *
class Geometrical:
    def __init__(self,W,U,V,Psi_X,Psi_Y,A,B,Kx,Ky, k, h):
        self.W      = W       
        self.U      = U       
        self.V      = V       
        self.Psi_X  = Psi_X   
        self.Psi_Y  = Psi_Y   
        self.A      = A       
        self.B      = B       
        self.Kx     = Kx      
        self.Ky     = Ky
        self.k      = k      
        self.h      = h
        self.x, self.y, self.z = symbols('x y z')  
        self.curves()
        self.Tetta()
        self.Eps()
        self.Gamma()
        
    def __f(self):
        return 6 * (1 / 4 - self.z ** 2 / self.h ** 2)
    def Tetta(self):
        self.Tetta_1 = Symbol("")
        self.Tetta_2 = Symbol("")
        self.Tetta_1 = -(diff(self.W, self.x))/self.A - self.Kx*self.U
        self.Tetta_2 = -(diff(self.W, self.y))/self.B - self.Ky*self.V
    def curves(self):
        self.Xi_1 = Symbol("")
        self.Xi_1 = (1/self.A) * diff(self.Psi_X, self.x) + (1/(self.A*self.B))*diff(self.A, self.y) *self.Psi_Y
        self.Xi_2 = Symbol("")
        self.Xi_2 = (1/self.B) * diff(self.Psi_Y, self.y) + (1/(self.A*self.B))*diff(self.B, self.x) *self.Psi_X
        self.Xi_12 = Symbol("")
        self.Xi_12 = 1/2 * ((diff(self.Psi_Y, self.x))/self.A + (diff(self.Psi_X, self.y))/self.B-((diff(self.A, self.y))*self.Psi_X + diff(self.B, self.x)*self.Psi_Y)/(self.A*self.B))
    def Eps(self):
        self.Eps_X = Symbol("")
        self.Eps_Y = Symbol("")
        self.Eps_ZX = Symbol("")
        self.Eps_ZY = Symbol("")
        self.Eps_X = diff(self.U,self.x)/self.A +self.V*diff(self.A, self.y)/(self.A*self.B) - self.Kx*self.W+(1/2)*self.Tetta_1**2
        self.Eps_Y = diff(self.V,self.y)/self.B +self.U*diff(self.B, self.x)/(self.A*self.B) - self.Ky*self.W+(1/2)*self.Tetta_2**2
        self.Eps_ZX = self.Xi_1 * self.z + self.Eps_X
        self.Eps_ZY = self.Xi_2 * self.z + self.Eps_Y
    def Gamma(self):
        self.Gamma_XZ = Symbol("")
        self.Gamma_YZ = Symbol("")
        self.Gamma_XY = Symbol("")
        self.Gamma_XZ = self.k * self.__f() * (self.Psi_X - self.Tetta_1)
        self.Gamma_YZ = self.k * self.__f() * (self.Psi_Y - self.Tetta_2)
        self.Gamma_XY = diff(self.V, self.x)/self.A + diff(self.U, self.y)/self.B -self.U*diff(self.A, self.y)/(self.A*self.B)-self.V*diff(self.B, self.x)/(self.A*self.B) + self.Tetta_1*self.Tetta_2