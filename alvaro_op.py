import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

#parametros y condiciones iniciales
be = 1/ (1.26 *10**(-3))
ce = 10**(-5)
w_0 = [1, 1]
t_0 = 0

#creamos funcion adhoc para la usar el ode de scipy
def EDO(t, w, b=be, c=ce):
    x, z = w
    return [(np.cos(t))/((2*b) + (c*z) - ((np.sin(t)/x))), (np.sin(t))/((2*b) + (c*z) - ((np.sin(t)/x)))]

#seteamos el la funcion ode para resolver el sistema de EDOS
r = ode(EDO)
r.set_integrator('dopri5') #comando para usar RK4
r.set_initial_value(w_0, t_0)

t = np.linspace(t_0, 7, 1000)

x = np.zeros(len(t))
z = np.zeros(len(t))

#iteramos usando la funcion ode antes mencionada
for i in range(len(t)):
    r.integrate(t[i])
    x[i], z[i] = r.y


#fig = plt.figure()

#plt.plot(t, z)
#plt.xlabel('theta')
#plt.ylabel('z')
#plt.title("Gotitaz")

fig = plt.figure()

plt.plot(x, z)
plt.xlabel('z')
plt.ylabel('x')
plt.title("Gotita")
plt.show()
