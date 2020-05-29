from numpy import array as ary; from numpy import log as ln
from numpy import cos, sin, pi, sqrt, exp, arccos, e
tau = 2*pi
import numpy as np;
from matplotlib import pyplot as plt

def plot_complex(*lines_data, **kwargs):
    for line in lines_data:
        plt.plot(np.real(line), np.imag(line), **kwargs)
    return

def expo(base, exponent):
    mag = ln(np.absolute(base))
    arg = np.angle(base)
    x = np.real(exponent)
    y = np.imag(exponent)
    return exp(x*mag-y*arg) * exp(1j* (x*arg + y*mag))

if __name__=='__main__':
    #make a cartesian grid
    # x0 = np.arange(-0,9)
    x0 = np.arange(-pi, pi, 0.2)
    y0 = np.arange(-pi, pi, 0.2)
    x_ = 0
    y_ = 1
    z_ = x_ + y_*1j
    # z_ = exp(1j*np.linspace(0, pi))

    vert_lines = ary(np.meshgrid(x0, y0*1j)).T.sum(axis=2)
    horiz_lines = ary(np.meshgrid(y0*1j, x0)).T.sum(axis=2)
    plt.style.use('dark_background')
    plot_complex(*horiz_lines, color='C0')
    plot_complex(*vert_lines, color='C0')

    plot_complex(*( expo(horiz_lines, z_) ))
    plot_complex(*( expo(vert_lines, z_) ))
    plt.show()