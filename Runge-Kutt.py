from matplotlib import pyplot as plt
import numpy
#y' = f(x, y), y(x0) = y0
x0 = 0.0 #задать
y0 = 0.0 #задать
h = 0.001 #шаг сетки Х

def crap(x, y):
    return 2.0 * x

def nexty(f_x_y, h, xn, yn):
    k1 = f_x_y(xn,yn)
    k2 = f_x_y(xn + h/2.0, yn + (h/2.0)*k1)
    k3 = f_x_y(xn + h/2, yn + (h/2)*k2)
    k4 = f_x_y(xn + h, yn + h*k3)
    yn = yn + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    return yn

def solveEquation():
    xVector = []
    yVector = []
    for _ in range(10000):
        xVector.append(0)
        yVector.append(0)
    xVector[0] = x0
    yVector[0] = y0
    for i in range(len(xVector)-1):
        yVector[i+1] = nexty(crap, h, xVector[i], yVector[i])
        xVector[i+1] = xVector[i]+h
    plt.plot(xVector, yVector)
    plt.show()
    # for i in range(len(xVector)):
    #     print("x:{0} y:{1};   ".format(xVector[i], yVector[i]))

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(linewidth=1)
solveEquation()

#
# for i in range(0, int(10.0/h)):
#     if i % (1.0/h) == 0:
#         print("x = " + str(xn) + ", y = " + str(yn))
#     xn+=h
#     nexty()
