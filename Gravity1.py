# First try to set up a gravity simulator in which two or more dots circle each other
# Jelmer Mulder

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import math

def askinput():
    try:
        waarde = int(input())
    except ValueError:
        waarde = input('Een integer graag: ')
    return waarde


# global variables
# constants
G = 20 #6.67428 * 10**(-11)
dt = 0.01

# particles info
masses = []
xlocation = []
ylocation = []
xspeed = []
yspeed = []

print('Hoe veel planeten?')
numplan = askinput()

for i in range(numplan):
    print('De massa van object {} is:'.format(i))
    mass = askinput()
    print('De x-coordinaat van object {} is:'.format(i))
    xcord = askinput()
    print('De y-coordinaat van object {} is:'.format(i))
    ycord = askinput()
    print('De x-snelheid van object {} is:'.format(i))
    xcomp = askinput()
    print('De y-snelheid van object {} is:'.format(i))
    ycomp = askinput()
    masses.append(mass)
    xlocation.append(xcord)
    ylocation.append(ycord)
    xspeed.append(xcomp)
    yspeed.append(ycomp)

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
    # particle 0 - sun
    xforce0, yforce0 = grav_force(xlocation[0], ylocation[0], xlocation[1], ylocation[1], masses[0], masses[1], G) # first coord are primare object - particle 0
    dx0, xspeed[0] = displacement(xforce0, masses[0], xspeed[0], dt)
    dy0, yspeed[0] = displacement(yforce0, masses[0], yspeed[0], dt)
    # update location particle 0
    xlocation[0] += dx0
    ylocation[0] += dy0

    # particle 1
    xforce1, yforce1 = grav_force(xlocation[1], ylocation[1], xlocation[0], ylocation[0], masses[1], masses[0], G) # first coord are primare object- particle 1
    dx1, xspeed[1] = displacement(xforce1, masses[1], xspeed[1], dt)
    dy1, yspeed[1] = displacement(yforce1, masses[1], yspeed[1], dt)
    # update location particle 1
    xlocation[1] += dx1
    ylocation[1] += dy1
    '''# particle 2
    xforce2, yforce2 = grav_force(xlocation[2], ylocation[2], xlocation[0], ylocation[0], masses[2], masses[0], G)
    dx2, xspeed[2] = displacement(xforce2, masses[2], xspeed[2], dt)
    dy2, yspeed[2] = displacement(yforce2, masses[2], yspeed[2], dt)
    # update location particle 2
    xlocation[2] += dx2
    ylocation[2] += dy2'''

    # plot the two dots using matplotlib
    plt.plot(xlocation[0], ylocation[0], 'ro', xlocation[1], ylocation[1], 'go')
    plt.xlim(-120, 120)
    plt.ylim(-120, 120)
    plt.draw()
    plt.pause(0.000001)
    plt.clf()
