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


c1 = 1
c2 = 2
b = 1


def y_true(x, b):
    c1 = 1
    x1, z1 = res_edo(b, c1)
    for i in range(0, len(z1-1)):
        if x == x1[i]:
            return z1[i]


def y_aprox(x, b, c2):
    x2, z2 = res_edo(b, c2)
    for i in range(0, len(z2-1)):
        if x == x2[i]:
            return z2[i]


def resid(p, x_num, x_exp):
    b, c2 = p
    err = x_exp - x_num
    return err

real = b, c1
p0 = b, c2
aprox = leastsq(resid, p0)
print aprox
print real
