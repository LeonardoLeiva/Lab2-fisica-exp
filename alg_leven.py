#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
primer intento de usar alg_leven
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

'''
def y_aprox(x, b, c1):
#    funcion que entrega un z para todo x mediante una extrapolacion simple de
#    los valores que no esten en el arreglo.
#    funcion que representa lo numerico
    x1, z1 = res_edo(b, c1)
    r = np.zeros(len(z1))
    for i in range(0, len(z1)- 2):
        if x == x1[i]:
            return z1[i]
        if (x > x1[i] and x < x1[i+1]) or (x < x1[i] and x > x1[i+1]):
            m = (x1[i+1] - x1[i])/ (z1[i+1] - z1[i])
            z = m* (x - x1[i]) + z1[i]
            return z
        r[i] = np.fabs(x - x1[i])
    r[-1] = np.fabs(x - x1[-1])
    n = np.where(r == r.min())
    return z1[n]
'''



def y_true(xv, b):
    c = 1
    x1, z1 = res_edo(b, c)
    r = np.zeros(len(z1))
    z = np.zeros(len(xv))
    for j in range(0, len(x) - 1):
        for i in range(0, len(z1) - 2):
            if x == x1[i]:
                z[j] = z1[i]
            elif (x > x1[i] and x < x1[i+1]) or (x < x1[i] and x > x1[i+1]):
                m = (x1[i+1] - x1[i])/ (z1[i+1] - z1[i])
                zj = m* (x - x1[i]) + z1[i]
                z[j] = z1[i]
            r[i] = np.fabs(x - x1[i])
        r[-1] = np.fabs(x - x1[-1])
        n = np.where(r == r.min())
        z[j] = z2[n]
    return z






    '''
    c = 1
    x2, z2 = res_edo(b, c)
    for i in range(0, len(z2-1)):
        if x == x2[i]:
            return z2[i]
    '''

x2, z2 = res_edo(b, c)
def y_aprox(x, b, c):
    x2, z2 = res_edo(b, c)
    return z2


def resid(p, z_exp, x2):
    b, c1 = p
    z_num = y_aprox(x2, b, c1)
    err = z_exp - z_num
    return err


x = np.arange(x2[len(x2)-1], x2[1], 20)
real = b, c
p0 = b, c1
aprox = leastsq(resid, p0, args=(y_aprox, x2))
print aprox [0]
print real
