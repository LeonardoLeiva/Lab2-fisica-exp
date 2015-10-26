#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class Perfil(object):
    '''

    '''


    def __init__(self, cond_ini, phi_ini = 0, c=0, b = 0):

        self.r_actual = cond_ini
        self.phi_actual = phi_ini
        self.c = c
        self.b = b


    def edos(self, dr = np.array([0, 0])):
        '''
        Ecuaciones para resolver
        '''

        x, z = self.r_actual
        phi = self.phi_actual
        d_x = dr[0]
        d_z = dr[1]
        x = x + d_x
        z = z + d_z
        dx = np.cos(phi)/ (2* self.b + self.c* z - (np.sin(phi))/ x)
        dz = np.sin(phi)/ (2* self.b + self.c* z - (np.sin(phi))/ x)
        return [dx, dz]


    def avanza_rk4(self, dt):
        '''
        Toma la condición actual del perfil y avanza su posicion en x y z
        en un intervalo de tiempo dt usando el método de rk4. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        x1, z1 = self.edos()
        k1_x = dt* x1
        k1_z = dt* z1

        x2, z2 = self.edos([k1_x/2., k1_z/2.])
        k2_x = dt* x2
        k2_z = dt* z2

        x3, z3 = self.edos([k2_x/2., k2_z/2.])
        k3_x = dt* x3
        k3_z = dt* z3

        x4, z4 = self.edos([k3_x, k3_z])
        k4_x = dt* x4
        k4_z = dt* z4

        x, z = self.r_actual
        xn = x + (k1_x + 2* k2_x + 2* k3_x + k4_x)/6.
        zn = z + (k1_z + 2* k2_z + 2* k3_z + k4_z)/6.
        self.r_actual = [xn, zn]
        self.phi_actual += dt
