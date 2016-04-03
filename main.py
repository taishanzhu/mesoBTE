
import numpy as np
import random
import matplotlib.pyplot as plt

sigma = 0.5
probability_scatter = 0.05


class Particle():
    def __init__(self,xpos=0, ypos=0, vx=0, vy=0):
        self.xpos = random.random()
        self.ypos = random.random()
        self.vx = np.random.randn() * sigma**2
        self.vy = np.random.randn() * sigma**2


class Material():
    def __init__(self):
        self.e_array = []
        for i in range(0, 11):   #initial_amount of e (user_input)
            a = Particle()
            self.e_array.append(a)

    def electron_amount(self, t):
        y = int(10*np.exp(-t))
        return y

    def electron_input(self, t):
        # self.e_array = []
        for i in range(self.electron_amount(t)):
            b = Particle
            b.xpos = 0
            b.ypos = random.random()
            b.vx = np.random.randn() * sigma**2
            b.vy = np.random.randn() * sigma**2
            self.e_array.append(b)

    def scatter(self, dt):
        # updating position
        for i in range(len(self.e_array)):
            self.e_array[i].xpos = self.e_array[i].xpos + self.e_array[i].vx * dt
            self.e_array[i].ypos = self.e_array[i].ypos + self.e_array[i].vy * dt
        # bouncing back
            if self.e_array[i].ypos >= 1:
                dy = self.e_array[i].ypos - 1
                self.e_array[i].ypos = self.e_array[i].ypos - 2*dy
                self.e_array[i].vy = - self.e_array[i].vy
            elif self.e_array[i].ypos <=0:
                dy = 0 - self.e_array[i].ypos
                self.e_array[i].ypos = self.e_array[i].ypos + 2*dy
                self.e_array[i].vy = - self.e_array[i].vy
        # update velocity
        length = int(len(self.e_array)* probability_scatter)
        for i in range(length):
            random_index = random.randint(0, len(self.e_array) - 1)
            self.e_array[random_index].xv = np.random.randn() * sigma**2
            self.e_array[random_index].yv = np.random.randn() * sigma**2
        # passing through if x<0 or x>1
        self.e_array = list(filter(lambda x: (x.xpos < 1) and (x.xpos > 0), self.e_array))

t = 0
dt = 0.1
simulation_duration = 1
mat = Material()
while t <= simulation_duration:
    mat.electron_input(t)
    mat.scatter(dt)
    t = t + dt
    for i in range(len(mat.e_array)):
        plt.plot(mat.e_array[i].xpos, mat.e_array[i].ypos, 'ro')
        plt.plot([mat.e_array[i].xpos, mat.e_array[i].xpos + mat.e_array[i].vx*dt], [mat.e_array[i].ypos, mat.e_array[i].ypos + mat.e_array[i].vy*dt], c='b', ls='-')
    plt.show()



