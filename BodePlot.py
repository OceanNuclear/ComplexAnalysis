#!/home/ocean/anaconda3/bin/python3
from numpy import e, cos, arccos, sin, arctan, tan, pi, sqrt, angle, prod; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt


def GH(s): #the input is supposed to be s= i*(omega) where omega is a purely real number.
	zeroes= [1]
	poles = [0.0001,2,4]
	const = 3
	numinator = [(1+(s/wb)) for wb in zeroes]
	denominator=[(1+(s/wb)) for wb in poles ]
	const_mod = const*prod(poles)/prod(zeroes)
	return const*prod(numinator)/prod(denominator)

omega = np.logspace(-5, 5, 200, base=10 )	#the imaginary axis of the laplace transform
response = [GH(1j*w) for w in omega]#plot the response
Gain= np.absolute(response)
arg = angle(response)

#plt.plot(omega,Gain)
plt.loglog(omega,Gain, basex=10, basey=10)
plt.title("Gain")
plt.show()
#plt.plot(omega,arg)
plt.semilogx(omega,arg, basex=10)
plt.title("phase")
plt.show()