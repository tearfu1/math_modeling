import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax = plt.axes(xlim = (-25, 25), ylim = (-25, 25))
line, = ax.plot([],[])


t = np.arange(0, 4*np.pi, 0.1)
    
x = 12*np.cos(t) + 8*np.cos(1.5*t)
y = 12*np.sin(t) - 8*np.sin(1.5*t)
    
def animate(i):
    z = 0.4 * i
    
    X = x*np.cos(z) - y*np.sin(z)
    Y = y*np.cos(z) + x*np.sin(z)

    line.set_data(X,Y)
    return line,

plt.title('krab')
anim = FuncAnimation(fig, animate, frames = 500, 
                                   interval =20, blit =True)

anim.save('123.gif' )