#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
2do intento algoritmo levenberg. funcional, pero no entrega lo que se espera.
'''

from perfil import Perfil
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq


def res_edo(c, b):
    '''
    Calcula edo numericamente dados c, b
    utiliza la clase perfil
    '''

    cond_ini = [0.0001, 0.0001]
    #phi_ini = -np.pi/2.
    p = Perfil(cond_ini, c, b)
    N= 100     #3*np.int(1e4)
    dphi= np.pi/ N
    phi=np.linspace(0.0001 , np.pi/ 2., N)
    x=np.zeros(N)
    z=np.zeros(N)

    x[0]=cond_ini[0]
    z[0]=cond_ini[1]

    for n in range(1,N):
        p.avanza_rk4(dphi)
        x[n]=p.r_actual[0]
        z[n]=p.r_actual[1]

    return [x, z]


def y_num(zv, b, c):
    '''
    extrapolacion numerica de los valores de la edo resuelta
    representa los valores aproximados numericamente del problema
    '''
    x1, z1 = res_edo(b, c)
    x = np.interp(zv, z1, x1)
    return x


def y_exp(z, b):
    '''
    entrega los resultados para la edo con parametro c1
    es una funcion de prueba que reemplaza el rol de valores experimentales
    '''
    c1 = 0.0001
    x2, z2 = res_edo(b, c1)
    return x2


def resid(p, x_exp, x2):
    '''
    entrega la diferencia entre las medidas experimentales y las numericas
    '''
    b, c = p
    x_num = y_num(x2, b, c)
    err = x_exp - x_num
    return err

#parámetros adecuados segun lo experimental
b =  1/ (1.26 *10**(-3))
cr = 0.0001
c = 0.00001

x2, z2 = res_edo(b, c)
p_real = b, cr
p0 = b, c
y = y_exp(x2, b)
aprox = leastsq(resid, p0, args=(x2, z2))
print aprox[0]
print p_real
