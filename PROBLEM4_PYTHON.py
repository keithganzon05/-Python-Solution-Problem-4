import numpy as np
import matplotlib.pyplot as plt
Yi = float(input('Input the initial height in meters: '))
Vi = int(input('Input the magnitude of velocity in m/s: '))
angle = int(input('Input the angle in radians with respect to the +x-axis: '))
Ax = float(input('Input the x-component of the acceleration: '))
Ay = float(input('Input the y-component of the acceleration: '))

if Ay == 0:
    print('Invalid magnitude of acceleration. Input a non-zero magnitude.')
else:
    angle = angle*(np.pi/180)
    Viy = Vi*np.sin(angle)
    Vf = 0
    ti = np.abs((Vf - Viy)/Ay)
    tf = ti*2
    Vix = Vi*np.cos(angle)
    t = np.linspace(start = 0, stop = tf, num = 100)
    Y = Yi + Viy*t + .5*Ay*(t**2)
    X = Vix*t + .5*Ax*(t**2)
    plt.plot(X,Y)
    plt.grid()
    plt.xlabel('Distance(X),m')
    plt.ylabel('Height(Y),m')
    