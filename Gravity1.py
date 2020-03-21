from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import math

x, y = 0, 200
G = 20000 #6.67428 * 10**(-11)
dt = 0.001
mass1 = 2
mass2 = 20
xlocation = [0.9, -1]
ylocation = [1, -1]
time = 0

def grav_force(x1, y1, x2, y2, mass1, mass2, G):
    angle =  math.atan((y2 - y1)/(x2 - x1))      #deltay/deltax
    dr = max([((x1-x2)**2 + (y1-y2)**2)**0.5, 0.0001])
    print(dr)
    force = G * mass1 * mass2 / dr**2
    xforce = math.cos(angle) * force 
    yforce = math.sin(angle) * force
    if x1 < x2 and y1>y2:
        xforce = xforce
        yforce = yforce
    elif x1> x2 and y1> y2:
        xforce = -1 * xforce
        yforce = -1 * yforce
    elif x1 < x2 and y1 < y2:
        xforce = xforce
        yforce = yforce
    else:
        xforce = -1 * xforce
        yforce = -1* yforce
    return xforce, yforce

def displacement(force, mass, dt):
    # F = m a
    a = force / mass
    dx = 1/2 * a * dt**2
    return dx

for i in range(200):
    xforce, yforce = grav_force(xlocation[0], ylocation[0], xlocation[1], ylocation[1], mass1, mass2, G)
    dx1, dy1 = displacement(xforce, mass1, dt), displacement(yforce, mass1, dt)
    dx2, dy2 = 5* math.cos(time), 5* math.sin(time)
    xlocation[0] = xlocation[0]+ dx1
    ylocation[0] = ylocation[0]+ dy1
    xlocation[1] = dx2
    ylocation[1] =dy2
    time += 10* dt
    plt.plot(xlocation[0], ylocation[0], 'ro', xlocation[1], ylocation[1], 'go')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.draw()
    plt.pause(0.00001)
    plt.clf()


