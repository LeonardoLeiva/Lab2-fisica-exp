import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import leastsq


'''
mismo metodo que testing_1 pero con b, c variables. Se duda de la certeza de
los datos ya que, dada una solucion "real", entrega un b lejano al original.
'''


def EDO(t, r, b, c):
    x, z = r
    return [(np.cos(t)) / ((2 * b) + (c * z) - ((np.sin(t) / x))),
            (np.sin(t)) / ((2 * b) + (c * z) - ((np.sin(t) / x)))]


def res_edo(be, ce, w_0=[1,1], t_0=0):
    r = ode(EDO)
    r.set_integrator('dopri5') #comando para usar RK4
    r.set_initial_value(w_0, t_0)
    r.set_f_params(be, ce)

    t = np.linspace(t_0, 3, 1000)

    x = np.zeros(len(t))
    z = np.zeros(len(t))

    #iteramos usando la funcion ode antes mencionada
    for i in range(len(t)):
        r.integrate(t[i])
        x[i], z[i] = r.y
    return x, z


def y_num(zv, b, c):
    x1, z1 = res_edo(b, c)
    x = np.interp(zv, z1, x1)
    return x



def y_exp():
    '''
    lee los datos de un archivo txt y los transforma en matriz
    '''
    pass



def resid(p, y, z2):
    b, c = p
    y_aprox = y_num(z2, b, c)
    err = y - y_aprox
    return err


b =  1/ (1.26 *10**(-3))
c = 10**(5)
c_antzatz = 10000
x_exp, z_exp = y_exp()
p = b, c
p0 = b, c_antzatz
aprox = leastsq(resid, p0, args=(x_exp, z_exp))

print aprox[0]
print p
