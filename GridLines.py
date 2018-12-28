#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
import seaborn as sns

maxHeight=9.0
minHeight=-10
maxWidth=15.0
minWidth=-10
vertSpace=0.5
horiSpace=0.5
res = 1000	#resolution of each line
E = 30	#multiplication factor for expanding the viewing window

xline = []
yline = []
#^they will have np.shape==((max-min)/Space,2,res)
for height in np.arange(minHeight,maxHeight,vertSpace):	#same y value
	xline.append(ary([np.linspace(minWidth,maxWidth,res),np.linspace(height,height,res)]))
for width in np.arange(minWidth,maxWidth,horiSpace):	#same x value
	yline.append(ary([np.linspace(width,width,res),np.linspace(minHeight,maxHeight,res)]))

def transformLine(linepair):	#feed in array of shape (2,res)
	return ary([transformPoint(point) for point in linepair.T]).T
def transformPoint(coord):
	x,y=coord
	z = complex(x,y)
	func = lambda z : 2*(z+10)/((z-2)*(z-5))
	w = func(z)
	return [w.real,w.imag]
xline=[transformLine(linepair) for linepair in xline]
yline=[transformLine(linepair) for linepair in yline]
#plotting...
palette=iter(sns.light_palette("blue", n_colors=len(xline)))
ytick = iter(np.arange(minHeight,maxHeight,vertSpace))
for xy in xline:	#constant height
	plt.plot(xy[0],xy[1], label="y="+str(next(ytick)),color=next(palette))
palette=iter(sns.dark_palette("orange", n_colors=len(yline)))
xtick = iter(np.arange(minWidth,maxWidth,horiSpace))
for xy in yline:	#constant x
	plt.plot(xy[0],xy[1], label="x="+str(next(xtick)),color=next(palette))
#plt.legend()
plt.grid(True)
plt.xlim(E*minWidth,E*maxWidth)
plt.ylim(E*minHeight,E*maxHeight)
plt.legend(prop={'size': 5})
plt.show()