import numpy as np
import matplotlib.pyplot as plt

'''
lee archivo para importar valores de la posicion
'''

a=open("w1.txt","r")

zw1=[];xw1=[];

for linea in a:

    zw1.append(float(linea[3:16]))
    xw1.append(float(linea[19:32]))

zw1=list(reversed(zw1))
xw1=list(reversed(xw1))

zw1=np.array(zw1,dtype='double')
xw1=np.array(xw1,dtype='double')

n = np.where(xw1 == xw1.max())
print int(np.mean(n))
d = len(xw1) - int(np.mean(n)) # d= len(xw1) - n[-1]
xn = np.zeros(d)
zn = np.zeros(d)
j = 0
x0 = xw1[int(np.mean(n)) - 1]
y0 = zw1[int(np.mean(n)) - 1]
for i in range(int(np.mean(n)) - 1, len(xw1)-1):
    xn[j] = xw1[i] - x0
    zn[j] = zw1[i] - y0
    j = j + 1

fig = plt.figure()

plt.plot(zn, -xn)
plt.xlabel('z')
plt.ylabel('x')
plt.title("Gotita")
plt.show()
