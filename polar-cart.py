from numpy import array as ary; from numpy import log as ln
from numpy import cos, sin, pi, sqrt, exp, arccos;
tau = 2*pi
import numpy as np;
from matplotlib import pyplot as plt
import seaborn as sns

def get_colours(palette_index, stride=20):
    if palette_index == 0:
        palette = plt.get_cmap('viridis').colors
    elif palette_index==1:
        palette = plt.get_cmap('plasma').colors
    print("Number of colors offered = ", len(palette))
    print("using a stride of", stride)
    return palette[::stride]

def set_fig_get_ax():
    sns.set_style('dark')
    # plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    return ax

def plot_polar(ax):
    #plotting the iso-magnitude lines
    theta_cont = np.linspace(0, tau, 300)
    pal = get_colours(0)
    for ind, r in enumerate(exp(np.linspace(-1.8, 1.2, 10))):
        ax.plot( r*cos(theta_cont), r*sin(theta_cont), color=pal[ind] )

    radial_cont = np.linspace(0, 4.5)
    pal = get_colours(1)
    for ind, t in enumerate(np.linspace(0, tau, 8, endpoint=False)):
        ax.plot( radial_cont*cos(t), radial_cont*sin(t), color=pal[ind])

    ax.set_xlabel('Real')
    ax.set_ylabel('Imag')
    ax.set_title('Argand diagram of $z_1$')
    plt.savefig('polar.png')
    plt.close()
    return

def plot_cart(ax):
    y_cont = ary([-pi, pi])
    pal = get_colours(0)
    for ind, x in enumerate(x_lines:=np.linspace(-1.8, 1.2, 10)):
        plt.plot(y_cont - y_cont + x, y_cont, color=pal[ind])

    x_cont = ary([-1.8, 1.5])
    pal = get_colours(1)
    for ind, y in enumerate(y_lines:=np.linspace(-pi, pi, 9, endpoint=True)):
        plt.plot(x_cont, y - x_cont + x_cont, color=pal[ind])
    ax.set_xlabel('Real (log magnitude of $z_1$)')
    ax.set_ylabel('Imag (phase of $z_1$)')
    ax.set_title('exponent of $z_1$ (i.e. ln($z_1$))')
    plt.savefig('cartesian.png')
    plt.close()

if __name__=='__main__':
    plot_polar(set_fig_get_ax())
    plot_cart(set_fig_get_ax())
