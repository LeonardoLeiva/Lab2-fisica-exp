#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

'''

from perfil import Perfil
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
fig.clf()

cond_ini = [0.0001, 0.0001]   #[-512, 834]
#phi_ini = -np.pi/2.
c = 1.3745*10**(-5)
b = 1/ (1.26 *10**(-3))

p = Perfil(cond_ini, c, b)
N= 1000     #3*np.int(1e4)
phi_f = np.pi/ 8.
dphi= phi_f/ N
phi=np.linspace(0.0001 , phi_f, N)
x=np.zeros(N)
z=np.zeros(N)

x[0]=cond_ini[0]
z[0]=cond_ini[1]

for n in range(1,N):
    p.avanza_rk4(dphi)
    x[n]=p.r_actual[0]
    z[n]=p.r_actual[1]

print x
fig = plt.figure(1)
fig.clf()
ax = plt.subplot(111)
ax.plot(x, z, 'o')
plt.show()
plt.draw()
