from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

x, y = 0, 200
G = 2 #6.67428 * 10**(-11)
dt = 0.0001
massa = 1

xlocation = [-20, 20]
ylocation = [0, 0]

def walk(x, y):
    x = -1 + 2 * random.random()
    y = -1 + 2 * random.random()
    return x, y

for i in range(100):
    dx1, dy1 = walk(xlocation[0], ylocation[0])
    dx2, dy2 = walk(xlocation[1], ylocation[1])
    print(dx1)
    xlocation[0] = xlocation[0]+ dx1
    ylocation[0] = ylocation[0]+ dy1
    xlocation[1] = xlocation[1] + dx2
    ylocation[1] = ylocation[1] + dy2

    plt.plot(xlocation[0], ylocation[0], 'ro', xlocation[1], ylocation[1], 'go')
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    plt.draw()
    plt.pause(0.000001)
    plt.clf()


