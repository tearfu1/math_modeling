import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t = np.arange(0, 50, 0.01)
    
def kek(a,b,A,B,delta, t):
    x = A*np.sin(a*t+delta)
    y = B*np.sin(b*t)
    plt.plot(x,y)
    plt.savefig('kek2.png')
    
kek(1, 2, 1, 7, np.pi/2, t)


