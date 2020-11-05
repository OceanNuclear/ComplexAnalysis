#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt, e; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
import seaborn as sns
#uses arrows to plot where each point lands after being transformed by the function
LongComputationalTime = False
def complexFunc(point): #if LongComputationalTime == True
	[x,y] = point
	z = x+1j*y
	function = (z**2+4)/((z-3)*(z+1)*(z+6)*(z))
	return [np.real(function),np.imag(function)]
def complexInput(z): #if LongComputationalTime == False
	#RC=0.0000001
	function = -(z+1)/((z-2)*(z+3))
	#(z**2+4)/((z-3)*(z+1)*(z+6)*(z))
	return function

def mymeshgrid(x,y):
	coord = []
	for x1 in x:
		for y1 in y:
			coord.append([x1,y1])
	return np.array(coord).reshape([len(x)*len(y),2])

def rotateColorSpace(theta):
	#given a vector pointing at 1,0,0; we want to rotate it around the (1/sqrt(3))*[1,1,1] axis by theta degrees.
	w = cos(theta/2)
	x = sin(theta/2)/sqrt(3)
	y = sin(theta/2)/sqrt(3)
	z = sin(theta/2)/sqrt(3)

	A = ary([[ y*y+z*z, w*z-x*y,-w*y-x*z],
			 [-w*z-x*y, x*x+z*z, w*x-y*z],
			 [ w*y-x*z,-w*x-y*z, x*x+y*y]])
	R = np.identity(3)	# = identity matrix.
	R-= 2*A
	return (np.round(R@ary([1,0,0])))

x = np.linspace(-5,5, 50)
y = np.linspace(-5,5, 40)
startingPts = mymeshgrid(x,y)
#Oh yeah computer memory problem. Now I've got a wobble in my grid.
#startingPts = np.concatenate(np.transpose(np.meshgrid(x,y)), axis=0)
cycleLen=len(startingPts)
cycleLen=6
uncleanLandingPts = [complexFunc(z) for z in startingPts]
landingPts = np.array([z if np.isfinite(z).all() else [0,0] for z in uncleanLandingPts])
sortedLandingPoints = np.reshape(landingPts,[len(x),len(y),2])

colorcycle = iter([rotateColorSpace(theta) for theta in np.linspace(0,tau, cycleLen)])
#Order=FABCDEF
if LongComputationalTime:
	for n in range(len(startingPts)):
		plt.annotate("", xy=startingPts[n], xytext=landingPts[n],arrowprops=dict(color = next(colorcycle), arrowstyle= '<-', alpha=0.5,),)#use arrowheads
		#pass
	#plot the y direction gridlines landing location
	for n in range(len(x)):
		plt.plot(sortedLandingPoints[n,:,0],sortedLandingPoints[n,:,1], lw=0.8, alpha=1, color= "green")#next(colorcycle))
		#for n in range (int(len(y)/2)) :next(colorcycle)
	#for n in range (int(cycleLen/3)): next(colorcycle)	#shift the color cycle foward by 1/3
	#plot the x direction gridlines landing location
	for n in range(len(y)):
		plt.plot(sortedLandingPoints[:,n,0],sortedLandingPoints[:,n,1], lw=0.8, alpha=1, color= "red")#next(colorcycle))

	xmin = [min(startingPts[:,0]),min(landingPts[:,0])]
	xmax = [max(startingPts[:,0]),max(landingPts[:,0])]
	ymin = [min(startingPts[:,1]),min(landingPts[:,1])]
	ymax = [max(startingPts[:,1]),max(landingPts[:,1])]
	plt.xlim(  min (xmin) , max ( xmax )  )
	plt.ylim(  min (ymin) , max ( ymax )  )

	plt.show()
	plt.plot(landingPts[:,:]-np.ones(np.shape(landingPts[:,:])))
	plt.show()

Radius = 100
small = 0.001
st_line = np.linspace(0,0,100)-1j*np.logspace(np.log10(small),np.log10(Radius),100)
theta=np.linspace(-pi/2,pi/2,200)
theta_2 = theta[:int(len(theta)/2)]
theta_3 = theta[int(len(theta)/2):]
semiCirc= Radius*cos(theta)+1j*Radius*sin(theta)
smallCirc =small*cos(-theta_2)+1j*small*sin(-theta_2)
smallCirc2=small*cos(-theta_3)+1j*small*sin(-theta_3)
reverse_st = -st_line[::-1]
Dee = np.concatenate([smallCirc2,st_line,semiCirc,reverse_st,smallCirc])
color = sns.palettes.hls_palette(n_colors=6)
for n in range(0,6):
	segment=complexInput(Dee)[100*n:100*(n+1)]
	plt.plot(segment.real,segment.imag,color=color[n])
#plt.xlim(-1,1)
#plt.ylim(-1,1)
#plt.scatter(complexInput(Dee).real[::20],complexInput(Dee.imag)[::20])
plt.show()