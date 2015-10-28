import numpy as np
import matplotlib.pyplot as plt

'''
lee archivo para importar valores de la posicion
'''

a=open("w1.txt","r")

zw1=[];xw1=[];
zw2=[];xw2=[];
zw3=[];xw3=[];
zw4=[];xw4=[];
zo1=[];xo1=[];
zo2=[];xo2=[];
zo3=[];xo3=[];
zo4=[];xo4=[];
zs1=[];xs1=[];
zs2=[];xs2=[];
zs3=[];xs3=[];
zs4=[];xs4=[];

#for i in range(1,5,1):

for linea in a:

    zw1.append(float(linea[3:16]))
    xw1.append(float(linea[19:32]))

zw1=list(reversed(zw1))
xw1=list(reversed(xw1))

zw1=np.array(zw1,dtype='double')
xw1=np.array(xw1,dtype='double')

print zw1

print xw1

fig = plt.figure()

plt.plot(xw1, zw1)
plt.xlabel('z')
plt.ylabel('x')
plt.title("Gotita")
plt.show()
