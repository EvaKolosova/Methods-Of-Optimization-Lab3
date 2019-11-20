import numpy as np
from matplotlib import pylab
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize
from sympy import diff, symbols, cos, sin


def f(point):
 x, y = point
 return np.cos(x) * np.cos(y)


#Print func
x_min = 0
x_max = 10.0
dx = 0.1

x_list = np.arange(x_min, x_max, dx)

y_min = 0
y_max = 10.0
dy = 0.1

y_list = np.arange(y_min, y_max, dy)

xgrid, ygrid = np.meshgrid(x_list, y_list)

zgrid = np.cos(xgrid) * np.cos(ygrid)

fig = pylab.figure()
axes = Axes3D(fig)

axes.plot_surface(xgrid, ygrid, zgrid)
pylab.show()

#Scipy
x0 = [10, 20]
res = minimize(f, x0, tol=1e-6)
print("min X = ", res.x, "\n")

#Sympy

x, y = symbols('x y')
variables = (x, y)
symbol_func = cos(x) * cos(y)
derivatives = []
for variable in variables:
    derivatives.append(diff(symbol_func, variable))
print("x derivatives = ", derivatives[0], "\n")
print("y derivatives = ", derivatives[1])