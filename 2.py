import numpy as np
import matplotlib.pyplot as plt

def prikol(e=0.8, p=3):
    phi = np.arange(0, 2*np.pi,0.00001)
    r = p / (1+e*np.cos(phi))
    
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    
    plt.axis("equal")
    plt.plot(x,y)
    plt.savefig('hahah.png')
    
prikol()
    