# First try to set up a gravity simulator in which two or more dots circle each other
# Jelmer Mulder

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import math

# global variables
# constants
G = 20 #6.67428 * 10**(-11)
dt = 0.001

# particles info
mass1 = 2
mass2 = 2000
xlocation = [5, 0]
ylocation = [0, 0]
xspeed = [0, 0]
yspeed = [100, 0]

# Force function
def grav_force(x1, y1, x2, y2, mass1, mass2, G):
    angle =  math.atan((y2 - y1)/(x2 - x1))      #deltay/deltax
    dr = max(((x1-x2)**2 + (y1-y2)**2)**0.5, 0.2)
    force = G * mass1 * mass2 / dr**2
    xforce = math.cos(angle) * force 
    yforce = math.sin(angle) * force

    # The direction of force depends on relative location
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

# function which calculate a tiny displacement during dt seconds
def displacement(force, mass, v, dt):
    a = force / mass # F = m a
    v = v + a * dt
    dx = v * dt # dx = v0*dt + a * t * dt
    return dx, v

# for loop which draws the dots on a figure
for i in range(600):
    #particle 1
    xforce1, yforce1 = grav_force(xlocation[0], ylocation[0], xlocation[1], ylocation[1], mass1, mass2, G)
    dx1, xspeed[0] = displacement(xforce1, mass1, xspeed[0], dt)
    dy1, yspeed[0] = displacement(yforce1, mass1, yspeed[0], dt)
    # update location particle 1
    xlocation[0] += dx1
    ylocation[0] += dy1
    # particle 2
    xforce2, yforce2 = grav_force(xlocation[1], ylocation[1], xlocation[0], ylocation[0], mass1, mass2, G)
    dx2, xspeed[1] = displacement(xforce2, mass2, xspeed[1], dt)
    dy2, yspeed[1] = displacement(yforce2, mass2, yspeed[1], dt)
    # update location particle 2
    xlocation[1] += dx2
    ylocation[1] += dy2

    # plot the two dots using matplotlib
    plt.plot(xlocation[0], ylocation[0], 'ro', xlocation[1], ylocation[1], 'go')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.draw()
    plt.pause(0.000001)
    plt.clf()


