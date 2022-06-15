from types import LambdaType
import matplotlib.pyplot as plot
import numpy as np


# params
p = 1
a = 3



class Range:

    def __init__(self):
        self.start  = 0
        self.end    = 0

    def __init__(self, start: float, end: float):
        self.start  = start
        self.end    = end

    def to_str(self) -> str:
        return "(" + str(self.start) + ", " + str(self.end) + ")"

    def contains(self, x: float) -> bool:
        return (x >= self.start) and (x <= self.end)

circle = lambda x : np.sqrt(a**2 - x**2)

def ShowPlot(f: LambdaType, x_arange, captions: list = 0):

    fig, ax = plot.subplots()
    # ax.set_title("Root: " + str(root) + " +- " + str(accurasy))
    plot.grid(which='minor', color = 'k', linestyle = ':')
    plot.grid(which='major', color = 'k', linewidth = 1, linestyle = ':')
    grid_sizze = 1
    # ax.set_yticks(np.arange(0, f(range.start), f(range.start) / 10))
    ax.set_xticks(np.arange(0, x_arange[len(x_arange) - 1] + grid_sizze, grid_sizze))
    if (captions):
        ax.set_xlabel(captions[0])
        ax.set_ylabel(captions[1])
    plot.plot(x_arange, f(x_arange), "r")
    t_circ = np.arange(0, a + 0.001, 0.001)
    plot.plot(t_circ, circle(t_circ), "b")
    plot.show()

# x = a * cos(phi)
# y = a * sin(phi)
def _x(phi: float, rad: float) -> float :
    return rad * np.cos(phi)
def _y(phi: float, rad: float) -> float :
    return rad * np.sin(phi)

def ShowPlot_from_radial(f: LambdaType, phi_arange, captions: list = 0):

    fig, ax = plot.subplots()
    # ax.set_title("Root: " + str(root) + " +- " + str(accurasy))
    plot.grid(which='minor', color = 'k', linestyle = ':')
    plot.grid(which='major', color = 'k', linewidth = 1, linestyle = ':')
    grid_sizze = 1
    # ax.set_yticks(np.arange(0, f(range.start), f(range.start) / 10))
    # ax.set_xticks(np.arange(a - grid_sizze, a + grid_sizze, grid_sizze))
    if (captions):
        ax.set_xlabel(captions[0])
        ax.set_ylabel(captions[1])    
    plot.plot(_x(phi_arange, f(phi_arange) + a), _y(phi_arange, f(phi_arange) + a), "r")
    plot.plot(_x(phi_arange, a), _y(phi_arange, a), "b")
    plot.show()


def main():


    sig_xx = lambda r :  0.9 * p * (1 + a**2 / r**2) + 0.1 * p * (1 + 3 * a**4 / r**4)
    print(sig_xx(a))
    print(sig_xx(4*a))
    print(sig_xx(1000))
    ShowPlot(sig_xx, np.arange(a, 12, 0.01), ['r, мм', 'sig_xx, p'])


    

    sig_xx = lambda r :  0.9 * p * (1 - a**2 / r**2) + 0.1 * p * (1 - 4 * a**2 / r**2 + 3 * a**4 / r**4)
    print(sig_xx(a))
    print(sig_xx(4*a))
    print(sig_xx(1000))
    ShowPlot(sig_xx, np.arange(a, 12, 0.01), ['r, мм', 'sig_xx, p'])




    sig_yy = lambda r :  0.9 * p * (1 - a**2 / r**2) - 0.1 * p * (1 - 4 * a**2 / r**2 + 3 * a**4 / r**4)
    print(sig_yy(a))
    print(sig_yy(4*a))
    print(sig_yy(1000))
    ShowPlot(sig_yy, np.arange(a, 12, 0.01), ['r, мм', 'sig_yy, p'])




    sig_yy = lambda r :  0.9 * p * (1 + a**2 / r**2) - 0.1 * p * (1 + 3 * a**4 / r**4)
    print(sig_yy(a))
    print(sig_yy(4*a))
    print(sig_yy(1000))
    ShowPlot(sig_yy, np.arange(a, 12, 0.01), ['r, мм', 'sig_yy, p'])




    sig_ff = lambda phi :  1.8 * p - 0.4 * p * np.cos(phi)
    ShowPlot_from_radial(sig_ff, np.arange(0, np.pi / 2, 0.01), ['x', 'y'])




    sig_xx = lambda phi :  (1.8 * p - 0.4 * p * np.cos(2 * phi)) * np.sin(phi)**2
    sig_yy = lambda phi :  (1.8 * p - 0.4 * p * np.cos(2 * phi)) * np.cos(phi)**2
    sig_xy = lambda phi :  (-0.9 * p + 0.2 * p * np.cos(2 * phi)) * np.sin(2 * phi)
    sig_i = lambda phi :  np.sqrt( ( (sig_xx(phi) - sig_yy(phi))**2 + sig_yy(phi)**2 + sig_xx(phi)**2 + 6*sig_xy(phi)**2 ) / 2 )
    ShowPlot_from_radial(sig_i, np.arange(0, np.pi / 2, 0.01), ['x', 'y'])
    print(max(sig_i(np.arange(0, np.pi / 2, 0.0001))))
    print(min(sig_i(np.arange(0, np.pi / 2, 0.0001))))






if __name__ == "__main__":
    main()
