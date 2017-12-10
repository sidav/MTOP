from rk4 import SolverRK4
from matplotlib import pyplot as plt

f1 = lambda x, y, z: \
    2 * x

f2 = lambda x, y, z: \
    3 * x * x

solver = SolverRK4(f1, f2)
xr, yr = solver.solve([0, 0], 0.001, 10)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(linewidth=1)
plt.plot(xr, yr[0])
plt.plot(xr, yr[1])
plt.show()