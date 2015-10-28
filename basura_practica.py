import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import leastsq

'''
3er intento de algoritmo de levenberg. funcional, pero no como se espera
'''

def EDO(t, w, b, c):
    x, z = w
    return [(np.cos(t)) / ((2 * b) + (c * z) - ((np.sin(t) / x))),
            (np.sin(t)) / ((2 * b) + (c * z) - ((np.sin(t) / x)))]


def res_edo(be, ce, w_0=[1,1], t_0=0):
    #parametros y condiciones iniciales
    #be = 1/ (1.26 *10**(-3))
    #ce = 10**(-5)
    #w_0 = [1, 1]
    #t_0 = 0
    #creamos funcion adhoc para la usar el ode de scipy
    #seteamos el la funcion ode para resolver el sistema de EDOS
    r = ode(EDO)
    r.set_integrator('dopri5') #comando para usar RK4
    r.set_initial_value(w_0, t_0)
    r.set_f_params(b, c)

    t = np.linspace(t_0, 7, 1000)

    x = np.zeros(len(t))
    z = np.zeros(len(t))

    #iteramos usando la funcion ode antes mencionada
    for i in range(len(t)):
        r.integrate(t[i])
        x[i], z[i] = r.y
    return x, z


def x_num(zv, b, c):
    '''
    extrapolacion numerica de los valores de la edo resuelta
    representa los valores aproximados numericamente del problema
    '''
    x1, z1 = res_edo(b, c)
    x = np.interp(zv, z1, x1)
    return x


def x_exp(z, b):
    '''
    entrega los resultados para la edo con parametro c1
    es una funcion de prueba que reemplaza el rol de valores experimentales
    '''
    c1 = 10**(5)
    x2, z2 = res_edo(b, c1)
    x = np.interp(z, z2, x2)
    return x


def resid(p, x_ex, z2):
    '''
    entrega la diferencia entre las medidas experimentales y las numericas
    '''
    b, c = p
    x_aprox = x_num(z2, b, c)
    err = x_ex - x_aprox
    return err


b =  1/ (1.26 *10**(-3))
cr = 10**(5)
c = 105000

x2, z2 = res_edo(b, cr)
p_real = b, cr
p0 = b, c
x = x_exp(x2, b)
aprox = leastsq(resid, p0, args=(x, z2))
print aprox[0]
print p_real
