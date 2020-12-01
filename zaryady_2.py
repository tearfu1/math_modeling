import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

k = 8.98755*10**9

q1 = 1*10**(-6)
q2 = 1*10**(-6)
q3 = 1*10**(-6)
q4 = 1*10**(-6)
q5 = 1*10**(-6)

m1 = 1
m2 = 1
m3 = 1
m4 = 1
m5 = 1

t = np.arange(0, 5, 0.01)

def move_func(s,t):
    (x1,v_x1,y1,v_y1,
    x2,v_x2,y2,v_y2,
    x3,v_x3,y3,v_y3,
    x4,v_x4,y4,v_y4,
    x5,v_x5,y5,v_y5) = s
     
    dxdt1=v_x1
    dv_xdt1 = (k*q1*q2/m1*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5
                +k*q1*q3/m1*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5
                +k*q1*q4/m1*(x1-x4)/((x1-x4)**2+(y1-y4)**2)**1.5
                +k*q1*q5/m1*(x1-x5)/((x1-x5)**2+(y1-y5)**2)**1.5)
    dydt1=v_y1
    dv_ydt1 = (k*q1*q2/m1*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5
                +k*q1*q3/m1*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5
                +k*q1*q4/m1*(y1-y4)/((x1-x4)**2+(y1-y4)**2)**1.5
                +k*q1*q5/m1*(y1-y5)/((x1-x5)**2+(y1-y5)**2)**1.5)
     
    dxdt2=v_x2
    dv_xdt2 = (k*q2*q1/m2*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5
                +k*q2*q3/m2*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5
                +k*q2*q4/m2*(x2-x4)/((x2-x4)**2+(y2-y4)**2)**1.5
                +k*q2*q5/m1*(x2-x5)/((x2-x5)**2+(y2-y5)**2)**1.5)
    dydt2=v_y2
    dv_ydt2 = (k*q2*q1/m2*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5
                +k*q2*q2/m2*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5
                +k*q2*q4/m2*(y2-y4)/((x2-x4)**2+(y2-y4)**2)**1.5
                +k*q2*q5/m1*(y2-y5)/((x2-x5)**2+(y2-y5)**2)**1.5)
     
    dxdt3=v_x3
    dv_xdt3 = (k*q3*q1/m3*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5
                +k*q3*q2/m3*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5
                +k*q3*q4/m3*(x3-x4)/((x3-x4)**2+(y3-y4)**2)**1.5
                +k*q2*q5/m1*(x3-x5)/((x3-x5)**2+(y3-y5)**2)**1.5)
    dydt3=v_y3
    dv_ydt3 = (k*q1*q3/m3*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5
                +k*q3*q2/m3*(y3-y2)/((x3-x2)**2+(y3-y2)**2)**1.5
                +k*q3*q4/m3*(y3-y4)/((x3-x4)**2+(y3-y4)**2)**1.5
                +k*q3*q5/m1*(y3-y5)/((x3-x5)**2+(y3-y5)**2)**1.5)
    
    dxdt4=v_x4
    dv_xdt4 = (k*q4*q1/m4*(x4-x1)/((x4-x1)**2+(y4-y1)**2)**1.5
                +k*q4*q2/m4*(x4-x2)/((x4-x2)**2+(y4-y2)**2)**1.5
                +k*q4*q3/m4*(x4-x3)/((x4-x3)**2+(y4-y3)**2)**1.5
                +k*q4*q5/m1*(x4-x5)/((x4-x5)**2+(y4-y5)**2)**1.5)
    dydt4=v_y4
    dv_ydt4 = (k*q4*q1/m4*(y4-y1)/((x4-x1)**2+(y4-y1)**2)**1.5
                +k*q4*q2/m4*(y4-y2)/((x4-x2)**2+(y4-y2)**2)**1.5
                +k*q4*q3/m4*(y4-y3)/((x4-x3)**2+(y4-y3)**2)**1.5
                +k*q4*q5/m1*(y4-y5)/((x4-x5)**2+(y4-y5)**2)**1.5)
    
    dxdt5=v_x5
    dv_xdt5 = (k*q5*q1/m4*(x5-x1)/((x5-x1)**2+(y5-y1)**2)**1.5
                +k*q5*q2/m4*(x5-x2)/((x5-x2)**2+(y5-y2)**2)**1.5
                +k*q5*q3/m4*(x5-x3)/((x5-x3)**2+(y5-y3)**2)**1.5
                +k*q5*q4/m1*(x5-x4)/((x5-x4)**2+(y5-y4)**2)**1.5)
    dydt5=v_y5
    dv_ydt5 = (k*q5*q1/m4*(y5-y1)/((x5-x1)**2+(y5-y1)**2)**1.5
                +k*q5*q2/m4*(y5-y2)/((x5-x2)**2+(y5-y2)**2)**1.5
                +k*q5*q3/m4*(y5-y3)/((x5-x3)**2+(y5-y3)**2)**1.5
                +k*q5*q4/m1*(y5-y4)/((x5-x4)**2+(y5-y4)**2)**1.5)
     
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5)
 
    
    
x10=0
v_x10=0
y10=0
v_y10=0

x20=0
v_x20=0
y20=1
v_y20=0

x30=1
v_x30=0
y30=1
v_y30=0

x40=1
v_x40=0
y40=0
v_y40=0

x50=0.5
v_x50=0
y50=0.5
v_y50=0
 
s0=(x10, v_x10, y10, v_y10,
    x20, v_x20, y20, v_y20,
    x30, v_x30, y30, v_y30,
    x40, v_x40, y40, v_y40,
    x50, v_x50, y50, v_y50)

sol=odeint(move_func,s0,t)

fig=plt.figure()
bodys=[]

for i in range(0,len(t),1):
    body1, = plt.plot(sol[:i,0],sol[:i,2], '-',color='r')
    body1_line, = plt.plot(sol[i,0], sol[i,2],'o', color='r')
    
    body2, = plt.plot(sol[:i,4],sol[:i,6], '-',color='g')
    body2_line, = plt.plot(sol[i,4], sol[i,6],'o', color='g')
    
    body3, = plt.plot(sol[:i,8],sol[:i,10], '-',color='b')
    body3_line, = plt.plot(sol[i,8], sol[i,10],'o', color='b')
    
    body4, = plt.plot(sol[:i,12],sol[:i,14], '-',color='k')
    body4_line, = plt.plot(sol[i,12], sol[i,14],'o', color='k')
    
    body5, = plt.plot(sol[:i,16],sol[:i,18], '-',color='m')
    body5_line, = plt.plot(sol[i,16], sol[i,18],'o', color='m')
    
    bodys.append([body1,body1_line, body2,body2_line, body3,body3_line, 
                      body4,body4_line, body5,body5_line])
        
ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
ani.save('123.gif')