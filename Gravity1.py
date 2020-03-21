from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
x, y = 0, 200
G = 2 #6.67428 * 10**(-11)
dt = 0.0001
massa = 1

def val(x, y):
    x += random.choice([-1, 1])*random.random()
    y += random.choice([-1, 1])*random.random()
    return x, y

for i in range(100):
    x, y = val(x, y)
    plt.plot(x, y, 'ro')
    plt.xlim(-10, 10)
    plt.ylim(0, 300)
    plt.draw()
    plt.pause(0.000001)
    plt.clf()


