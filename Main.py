from rk4 import SolverRK4
from matplotlib import pyplot as plt
from math import sin, cos, exp, tanh

## Константушечки
l_max = 180.0
G = 1750.0
Gn = 3500.0
U = [None,
     15.19, 8.18, 13.198,
     3.543, 4723.7, 423.7,
     204.41, 0.000001466, 0.013,
     0.09, 0.000005428, 0.024,
     0.00000592
     ]

E = [None,
     25000.0, 25000.0, 25000.0, 25000.0,
     40000.0, 40000.0, 40000.0,
     20000.0, 20000.0, 20000.0, 20000.0, 20000.0, 20000.0]

m = [84.0, 56.0, 42.0, 28.0, 92.0, 16.0]
m0 = 18.0

q = [None, None, 78.0, 140.0, 140.0]

### Функции

def p(_l):
    return 5.0 - (_l / 60.0)

def sub_sum_for_v(x):
    sum = 0.0
    for i in range(6):
        sum += m[i]*x[i] / m0
    return sum


def v(l, x):
    sum = 0.0
    for i in range(6):
        sum += (m[i] * x[i]) / (x7(l) * ( G + Gn * sub_sum_for_v(x) ) )
    return 509.209 * p(l) * sum

def R(i, _x7):
    return U[i] * exp(23.0 - (E[i] / _x7))

def I(x_l_vector): ## <----- сделать, это она только притворяется готовой.
    num_sum = 0.0
    for j in range(2, 5):
        num_sum += q[j]*m[j-1] * x_l_vector[j-1]   # Хьюстон, у нас проблема: x[j] должно зависеть от L,
                                                # я так понимаю, это результат интегрирования -> это функция
    denom_sum = 0.0
    for j in range(6):
        denom_sum += m[j] * x_l_vector[j]           # Та же беда

    return num_sum / denom_sum

### x7 ненаглядная


def x7(l):
    # if l == 0:
    #     return 373.0
    # elif l == 180.0:
    #     return 1500.0
    # else:

    # return alpha
    #res = l ** _alpha + 373
    # res = 373.0 + alpha*(sin(0.01*l))

    res = 1127 * tanh(alpha * l) + 373

    if 373.0 <= res <= 1500.0:
        return res
    else:
        print("OMG ERROR x7 IS FUCKING {0}".format(res))
        return 1500

################################################
### Система


dx1dl = lambda l, x1, x2, x3, x4, x5, x6: \
    - ( R(1, x7(l)) + R(2, x7(l)) + R(3, x7(l)) + R(4, x7(l)) ) * x1  * v(l, [x1, x2, x3, x4, x5, x6])

dx2dl = lambda l, x1, x2, x3, x4, x5, x6: \
    ( R(3, x7(l)) * x1 - (R(6, x7(l)) + R(7, x7(l)) + R(10, x7(l)) + R(13, x7(l)))*x2 ) * v(l, [x1, x2, x3, x4, x5, x6])

dx3dl = lambda l, x1, x2, x3, x4, x5, x6: \
    ( R(2, x7(l)) * x1 + R(6, x7(l))*x2 - ( R(5, x7(l)) + R(9, x7(l)) + R(12, x7(l)) )*x3) * v(l, [x1, x2, x3, x4, x5, x6])

dx4dl = lambda l, x1, x2, x3, x4, x5, x6: \
    ( R(1, x7(l))*x1 + R(7, x7(l)) * x2 + R(5, x7(l)) * x3 - (R(8, x7(l)) + R(11, x7(l)))*x4 ) * v(l, [x1, x2, x3, x4, x5, x6])

dx5dl = lambda l, x1, x2, x3, x4, x5, x6: \
    ( R(10, x7(l))*x2 + R(9, x7(l))*x3 + R(8, x7(l))*x4) * v(l, [x1, x2, x3, x4, x5, x6])

dx6dl = lambda l, x1, x2, x3, x4, x5, x6: \
    ( R(4, x7(l))*x1 + R(13, x7(l))*x2 + R(12, x7(l))*x3 + R(11, x7(l))*x4) * v(l, [x1, x2, x3, x4, x5, x6])


##########################################
########## Собственно, решение: ##########
##########################################

def solve_eq():
    solver = SolverRK4(dx1dl, dx2dl, dx3dl, dx4dl, dx5dl, dx6dl)
    lr, xr = solver.solve([1, 0, 0, 0, 0, 0], 0.5, l_max)

    last_x_index = len(xr[0]) - 1
    x_l = []
    for i in range(6):
        x_l.append(xr[i][last_x_index])
    # print(x_l)
    return x_l

def find_imax_by_bisection(a_min, a_max):
    global alpha
    eps = 0.00001
    diff = 9999.0
    alpha = a_min
    possibru_res = 0.0
    while(diff > eps):
        mean = (a_max + a_min) / 2.0
        mean_left = (mean + a_min) / 2.0
        mean_right  = (a_max + mean) / 2.0
        # слева
        alpha = mean_left
        left_res = I(solve_eq())
        # справа
        alpha = mean_right
        right_res = I(solve_eq())
        diff = abs(left_res - right_res)

        # print("left m{0} alf, right {}".format())

        if left_res > right_res:
            a_max = mean
            possibru_res = left_res
        else:
            a_min = mean
            possibru_res = right_res
    print("Max I() is {0}, at alpha = {1} ".format(possibru_res, alpha))


########################################
##### выполнение начинается отсюда #####
alpha = 373.0
find_imax_by_bisection(373.0, 1500.0)

# alpha = 959.0
# print(I(solve_eq()))

# plt.xlim(0, 180)
# plt.ylim(373, 1500)
# plt.grid(linewidth=1)
#
# alpha = 1.354
#
# h = 0.01
# curl = 0.0
# ls = []
# xs = []
# while curl <= 180.0:
#     ls.append(curl)
#     xs.append(x7(alpha, curl))
#     curl += h
#     pass
# plt.plot(ls, xs)
# plt.show()