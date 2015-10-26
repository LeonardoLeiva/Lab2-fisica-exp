#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

'''

from perfil import Perfil
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
fig.clf()

cond_ini = [1, 1]
c = 1
b = 1

p = Perfil(cond_ini, c, b)
N= 100     #3*np.int(1e4)
dphi=np.pi/ N
phi=np.linspace(0, np.pi, N)
x=np.zeros(N)
z=np.zeros(N)

x[0]=cond_ini[0]
z[0]=cond_ini[1]

for n in range(1,N):
    p.avanza_rk4(dphi)
    x[n]=p.r_actual[0]
    z[n]=p.r_actual[1]
print phi
print x
print z


fig = plt.figure(1)
fig.clf()
ax = plt.subplot(111)
ax.plot(x, z)
plt.show()
plt.draw()

'''
ax1=fig.add_subplot(211)
ax1.plot(x,y)
ax2=fig.add_subplot(212)
ax2.plot(t,E)
ax1.set_xlabel('Posicion en el eje X')
ax1.set_ylabel('Posicion en el eje Y')
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Energia total')
plt.draw()
plt.show()
'''
