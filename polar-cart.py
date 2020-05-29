from numpy import array as ary; from numpy import log as ln
from numpy import cos, sin, pi, sqrt, exp, arccos;
tau = 2*pi
import numpy as np;
from matplotlib import pyplot as plt
import seaborn as sns


def set_fig_get_ax():
    sns.set_style('dark')
    # plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    return ax

def plot_polar(ax):
    #plotting the iso-magnitude lines
    theta_cont = np.linspace(0, tau, 300)
    for r in exp(np.linspace(-1.8, 1.2, 10)):
        ax.plot( r*cos(theta_cont), r*sin(theta_cont), color='C0' )

    radial_cont = np.linspace(0, 4.5)
    for t in np.linspace(0, tau, 8, endpoint=False):
        ax.plot( radial_cont*cos(t), radial_cont*sin(t), color='C1')

    ax.set_xlabel('Real')
    ax.set_ylabel('Imag')
    ax.set_title('Argand diagram of z')
    plt.savefig('polar.png')
    plt.close()
    return

def plot_cart(ax):
    y_cont = ary([-pi, pi])
    for x in (x_lines:=np.linspace(-1.8, 1.2, 10)):
        plt.plot(y_cont - y_cont + x, y_cont, color='C0')

    x_cont = ary([-1.8, 1.5])
    for y in (y_lines:=np.linspace(-pi, pi, 9, endpoint=True)):
        plt.plot(x_cont, y - x_cont + x_cont, color='C1')
    ax.set_xlabel('Real (magnitude of z)')
    ax.set_ylabel('Imag (phase of z)')
    ax.set_title('exponent of z (i.e. ln(z))')
    plt.savefig('cartesian.png')
    plt.close()

if __name__=='__main__':
    plot_polar(set_fig_get_ax())
    plot_cart(set_fig_get_ax())
