import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import leastsq

'''
funcion generica para obtener la aproximacion c para cada set de datos exp
aun no es funcional
'''

def EDO(t, r, b, c):
    '''
    define la edo a resolver. t es el tiempo, r son las coordenadas, b y c los
    parametros a optimizar
    '''
    x, z = r
    return [(np.cos(t)) / ((2 * b) + (c * z) - ((np.sin(t) / x))),
            (np.sin(t)) / ((2 * b) + (c * z) - ((np.sin(t) / x)))]


def res_edo(ce, w_0=[1,1], t_0=0):
    '''
    resuelve la edo con dopri5 (rk4) mediante un resolvedor
    '''
    be = 1/ (1.26 *10**(-3))
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


def y_num(zv, c):
    '''
    resuelve la edo para c e interpola los resultados para zv
    '''
    b =  1/ (1.26 *10**(-3))
    x1, z1 = res_edo(c)
    x = np.interp(zv, z1, x1)
    return x


def y_exp(w):
    '''
    lee los datos de un archivo txt y los transforma en matriz
    '''
    a=open("w1.txt","r")

    zw1=[];xw1=[];

    for linea in a:

        zw1.append(float(linea[3:16]))
        xw1.append(float(linea[19:32]))

    zw1=list(reversed(zw1))
    xw1=list(reversed(xw1))

    zw1=np.array(zw1,dtype='double')
    xw1=np.array(xw1,dtype='double')

    n = np.where(xw1 == xw1.max())
    print int(np.mean(n))
    d = len(xw1) - int(np.mean(n)) # d= len(xw1) - n[-1]
    xn = np.zeros(d)
    zn = np.zeros(d)
    j = 0
    x0 = xw1[int(np.mean(n)) - 1]
    y0 = zw1[int(np.mean(n)) - 1]
    for i in range(int(np.mean(n)) - 1, len(xw1)-1):
        xn[j] = xw1[i] - x0
        zn[j] = zw1[i] - y0
        j = j + 1


def resid(p, y, z2):
    '''
    definicion de la funcion resta para optimizarla con leastsq
    '''
    c = p
    y_aprox = y_num(z2, c)
    err = y - y_aprox
    return err


def get_c_aprox(w, c0, b):
    c_antzatz = 10 ** (1)
    x_exp, z_exp = y_exp()
    p0 = c_antzatz
    aprox = leastsq(resid, p0, args=(x_exp, z_exp))

    print aprox[0]
    print p0



b =  1/ (1.26 *10**(-3))
