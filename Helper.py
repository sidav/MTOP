from rk4 import SolverRK4
from matplotlib import pyplot as plt
from math import sin, cos, exp

def x7(_alpha, l):
    # if l == 0:
    #     return 373.0
    # elif l == 180.0:
    #     return 1500.0
    # else:

    res = l ** alpha + 373
    # res = 373.0 + _alpha*(sin(0.01*l))

    if 373.0 <= res <= 1500.0:
        return res
    else:
        print("OMG ERROR x7 IS FUCKING {0}".format(res))
        return 1500


plt.xlim(0, 180)
plt.ylim(373, 1500)
plt.grid(linewidth=1)

alpha = 1.3

h = 0.01
curl = 0.0
ls = []
xs = []
while curl <= 180.0:
    ls.append(curl)
    xs.append(x7(alpha, curl))
    curl += h
    pass
plt.plot(ls, xs)
plt.show()