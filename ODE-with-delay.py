from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
#An attempt to investigate what happens when your ODE is y'(t)=y(t-Δt)
#i.e. a DDE (delayed differential equation)

total_time = 100 # total number of seconds to simulate
resolution = 100 # number of points to simulate per second
delay = 0.1 # how far back is Δt

def Seed_func(t):
    """
    The initial values of y, i.e. the boudnary condition.
    'dtsize' refers to how many elements of y to populate/calculate. 
    """
    return np.cos(t)

def dy_dx(y):
    """
    The function that translate y (a while ago) into dy/dx.
    """
    return y # using a identity formulat (x=y) here.

x = np.arange(0, total_time, 1/resolution)
seed = Seed_func(x[:int(delay*resolution)]) #seed the first few elements

y = list(seed).copy()
for t_ind in range(len(seed), len(x)):
    y.append( y[t_ind - int(delay*resolution)] + dy_dx(y[t_ind - int(delay*resolution)])*delay )

plt.ylabel("y(t)")
plt.xlabel("time")

plt.plot(x, y)
plt.show()
#Turns out, solving the ODE for numInt*delay elements is equivalent to integrating the seed values by numInt cycles.