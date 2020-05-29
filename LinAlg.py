from numpy import array as ary; from numpy import log as ln
from numpy import cos, sin, pi, sqrt, exp, arccos;
tau = 2*pi
import numpy as np;
from matplotlib import pyplot as plt

def plot_straight(*lines_data, **kwargs):
    for line in lines_data:
        plt.plot(line.T[0], line.T[1], **kwargs)
    return

if __name__=='__main__':
    '''
    This program was created solely for the prupose of visualizaing the transformation
    (x,-y
     y, x)
    '''

    x0 = np.arange(-5,5)
    y0 = np.arange(-3,3)
    vert_lines = ary(np.meshgrid(x0, y0)).T
    horiz_lines = ary(np.meshgrid(y0, x0))[::-1].T
    for y in np.linspace(-1.9, 1.9, 20):
        x = 1
        # x, y = [1, -1]
        M = ary([[x,-y], [y,x]])
        plot_straight(*[ary([M@point for point in line]) for line in vert_lines], color='C1')
        plot_straight(*[ary([M@point for point in line]) for line in horiz_lines], color='C2')
        plt.plot([0],[0], color='C1', label='vertical lines'); plt.plot([0],[0], color='C2',label='horizonal lines'); plt.legend()
        plt.title('y='+str(y)); plt.show()