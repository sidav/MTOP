from rk4 import SolverRK4
from matplotlib import pyplot as plt
from math import sin, cos

f1 = lambda t, x, y: \
    sin(x)*(-.1*cos(x) - cos(y))


f2 = lambda t, x, y: \
    sin(y) * (cos(x) - .1 * cos(y))

solver = SolverRK4(f1, f2)
xr, yr = solver.solve([1, 1], 0.001, 30)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(linewidth=1)
plt.plot(yr[0], yr[1])
#plt.plot(xr, yr[1])
plt.show()