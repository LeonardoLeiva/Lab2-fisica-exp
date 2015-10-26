#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

'''

from perfil import Perfil
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

fig=plt.figure()
fig.clf()


def res_edo(c, b):

    cond_ini = [-512, 824]
    #phi_ini = -np.pi/2.
    p = Perfil(cond_ini, c, b)
    N= 100     #3*np.int(1e4)
    dphi= np.pi/ N
    phi=np.linspace(0 , np.pi/ 2., N)
    x=np.zeros(N)
    z=np.zeros(N)

    x[0]=cond_ini[0]
    z[0]=cond_ini[1]

    for n in range(1,N):
        p.avanza_rk4(dphi)
        x[n]=p.r_actual[0]
        z[n]=p.r_actual[1]

    return [x, z]


c1 = 2
c = 1
b = 1


def y_aprox(x, b, c1):
    '''
    funcion que entrega un z para todo x mediante una extrapolacion simple de
    los valores que no esten en el arreglo.
    funcion que representa lo numerico
    '''
    x1, z1 = res_edo(b, c1)
    r = np.zeros(len(z1))
    for i in range(0, len(z1-2)):
        if x == x1[i]:
            return z1[i]
        if (x > x1[i] & x < x1[i+1]) | (x < x1[i] & x > x1[i+1]):
            m = (x1[i+1] - x1[i])/ (z1[i+1] - z1[i])
            z = m* (x - x1[i]) + z1[i]
            return z
        r[i] = np.fabs(x - x[i])
    r[len(x1)] = np.fabs(x - x[len(x1)])
    n = np.where(r == r.min())
    return z[n]



def y_true(x, b):
    c = 1
    x1, z1 = res_edo(b, c)
    r = np.zeros(len(z1))
    for i in range(0, len(z1-2)):
        if x == x1[i]:
            return z1[i]
        elif (x > x1[i] & x < x1[i+1]) | (x < x1[i] & x > x1[i+1]):
            m = (x1[i+1] - x1[i])/ (z1[i+1] - z1[i])
            z = m* (x - x1[i]) + z1[i]
            return z
        r[i] = np.fabs(x - x[i])
    r[len(x1)] = np.fabs(x - x[len(x1)])
    n = np.where(r == r.min())
    return z[n]


    '''
    c = 1
    x2, z2 = res_edo(b, c)
    for i in range(0, len(z2-1)):
        if x == x2[i]:
            return z2[i]
    '''


def resid( p, z_exp, x2):
    b, c1 = p
    z_num = y_aprox(x2, b, c1)
    err = z_exp - z_num
    return err

x2, z2 = res_edo(b, c)
x = np.arange(x2[len(x2)-1], x2[1], 20)
real = b, c
p0 = b, c1
aprox = leastsq(resid, p0, args=(y_aprox, x))
print aprox [0]
print real
