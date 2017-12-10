#y' = f(x, y), y(x0) = y0
x0 = 2.0 #задать
y0 = 4.0 #задать
h = 0.00001 #шаг сетки Х
xn = x0
yn = y0

def f_x_y(x, y):
    return 2.0 * x

def nexty():
    global h, xn, yn
    k1 = f_x_y(xn,yn)
    k2 = f_x_y(xn + h/2.0, yn + (h/2.0)*k1)
    k3 = f_x_y(xn + h/2, yn + (h/2)*k2)
    k4 = f_x_y(xn + h, yn + h*k3)
    yn = yn + h/6 * (k1 + 2*k2 + 2*k3 + k4)


for i in range(0, int(10.0/h)):
    if i % (1.0/h) == 0:
        print("x = " + str(xn) + ", y = " + str(yn))
    xn+=h
    nexty()
