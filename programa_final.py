import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import leastsq


'''
Resolucion del problema dejando fijo b y optimizando el valor de c.
'''
# b = 1/ (1.26 *10**(-3))


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


def y_exp():
    '''
    lee los datos de un archivo txt y los transforma en matriz
    '''
    a=open("w1.txt","r")
    zw1=[];xw1=[];
    #for i in range(1,5,1):
    for linea in a:
        zw1.append(float(linea[3:16]))
        xw1.append(float(linea[19:32]))
    zw1=list(reversed(zw1))
    xw1=list(reversed(xw1))
    zw1=np.array(zw1,dtype='double')
    xw1=np.array(xw1,dtype='double')
    x = xw1 * 10**(-3)
    z = zw1 * 10**(-3)
    return x, z


def resid(p, y, z2):
    '''
    definicion de la funcion resta para optimizarla con leastsq
    '''
    c = p
    y_aprox = y_num(z2, c)
    err = y - y_aprox
    return err


b =  1/ (1.26 *10**(-3))
c_antzatz = 10 ** (4)
x_exp, z_exp = y_exp()
p0 = c_antzatz
aprox = leastsq(resid, p0, args=(x_exp, z_exp))

print aprox[0]
print p0
