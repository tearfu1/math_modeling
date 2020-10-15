import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

mju = 0.97
d = 0.2
h_0 = 0.5
#s_dno = (np.pi*d**2)/4
S = 0.0002 
g = 10


t = np.linspace(0, 50, 50)

def speed (h,t):
    
#    v = (mju*(2*g*h))**0.5
    
#    dhdt = -v * (s_dno / s_otv)
    dhdt = -(4*S*mju*(2*g*h)**0.5) / (np.pi*d**2)
    
    return dhdt



solve = odeint(speed, h_0, t)
plt.plot(t, solve[:,0])
plt.show()