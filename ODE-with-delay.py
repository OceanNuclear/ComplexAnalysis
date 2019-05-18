#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
#An attempt to investigate what happens when your ODE is y'(t)=y(t-Δt)
numInt=2#Number of times to integrate the function to; reason for its name will be apparent after plotting beings

arysize=10000
delay = 100

def MathematicalFunctionOfChoice(dtsize):#dtsize refers to how many elements of y to populate/calculate
	return np.cos(np.arange(dtsize))

y=np.zeros(arysize)#create empty array
y[:delay]=MathematicalFunctionOfChoice(delay)#seed the first few elements
for t in range(arysize-delay):
	time=t+delay
	y[time]=y[t]+y[time-1]

plt.ylabel("y(t)")
plt.xlabel("time")
plt.plot(y[:(numInt+1)*delay])
plt.show()
#Turns out, solving the ODE for numInt*delay elements is equivalent to integrating the seed values by numInt cycles.