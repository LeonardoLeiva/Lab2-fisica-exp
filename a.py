import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

'''

'''


#parametros
b = 1
c = 2

#funciones

dx= lambda o, x, z: np.cos(o)/(2* b + c* z - (np.sin(o))/x)
dz= lambda o, x, z: np.sin(o)/(2* b + c* z - (np.sin(o))/x)


def func(o,var):
    x,y=var #'var' debe incluir las coordenadas en 2 dimensiones
    xd=dx(o, x, z) #evalua los valores entregados para cada coordenada
    zd=dz(o, x, z)

    return [xd,zd]


#condiciones iniciales
x0=5; y0=8; o0=0
ci=[x0,y0] #crea un vector con los valores iniciales para ser consecuentes
#con ingresar las condiciones iniciales juntas en la funcion definida


r=ode(func)
r.set_integrator('dopri5',max_step=0.01)
r.set_initial_value(ci,o0)


o=np.linspace(o0,np.pi,100)
x=np.zeros(len(o))
z=np.zeros(len(o))

for i in range(len(o)):
    r.integrate(o[i])
    x[i],z[i]=r.y


fig1=plt.figure(1)
fig1.clf()
ax1=fig1.add_subplot(212)
ax1.plot(x,z)
plt.title('y(s) vs dy/ds')
ax1.set_xlabel('y')
ax1.set_ylabel('dy/ds')
plt.draw()
plt.show()

#print x
#print y
#print z
