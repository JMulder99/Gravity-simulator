from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import math

x, y = 0, 200
G = 20000 #6.67428 * 10**(-11)
dt = 0.001
mass1 = 5
mass2 = 5
xlocation = [-0.3, 0.3]
ylocation = [2, -2]

def grav_force(x1, y1, x2, y2, mass1, mass2, G):
    angle =  math.atan((y2 - y1)/(x2 - x1))      #deltay/deltax
    dr = ((x1-x2)**2 + (y1-y2)**2)**0.5
    force = G * mass1 * mass2 / dr**2
    xforce = math.cos(angle) * force 
    yforce = math.sin(angle) * force
    return xforce, yforce

def displacement(force, mass, dt):
    # F = m a
    a = force / mass
    dx = 1/2 * a * dt**2
    return dx

for i in range(2000):
    xforce, yforce = grav_force(xlocation[0], ylocation[0], xlocation[1], ylocation[1], mass1, mass2, G)
    dx1, dy1 = displacement(xforce, mass1, dt), displacement(yforce, mass1, dt)
    dx2, dy2 = 0, 0
    print(dx1)
    xlocation[0] = xlocation[0]+ dx1
    ylocation[0] = ylocation[0]+ dy1
    xlocation[1] = xlocation[1] + dx2
    ylocation[1] = ylocation[1] + dy2

    plt.plot(xlocation[0], ylocation[0], 'ro', xlocation[1], ylocation[1], 'go')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-5, 5)
    plt.draw()
    plt.pause(0.000001)
    plt.clf()


