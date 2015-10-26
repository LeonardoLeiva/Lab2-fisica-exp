#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

'''

from perfil import Perfil
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
fig.clf()

cond_ini = [0.01, 0.01]   #[-512, 834]
#phi_ini = -np.pi/2.
c = 3
b = 2

p = Perfil(cond_ini, c, b)
N= 1000     #3*np.int(1e4)
phi_f = np.pi/ 2.
dphi= phi_f/ N
phi=np.linspace(0.01 , phi_f, N)
x=np.zeros(N)
z=np.zeros(N)

x[0]=cond_ini[0]
z[0]=cond_ini[1]

for n in range(1,N):
    p.avanza_rk4(dphi)
    x[n]=p.r_actual[0]
    z[n]=p.r_actual[1]


fig = plt.figure(1)
fig.clf()
ax = plt.subplot(111)
ax.plot(phi, z, 'o')
plt.show()
plt.draw()
