import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

mju = 0.62
d = 0.003
D = 0.08
H = 0.11
h_0 = 0.11
#s_dno = (np.pi*d**2)/4
g = 10


t = np.linspace(0, 100, 500)

def speed (h,t):
    
    dhdt = -((mju*(2*g*h)**0.5)*np.pi*d**2*H) / (6*h**2*D)
    return dhdt

solve = odeint(speed, h_0, t)
plt.plot(t, solve[:,0])
plt.show()