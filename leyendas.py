import matplotlib.pyplot as plt
import math

def fun(x):     #funcion seno
    return math.sin(x)

x = [n for n in range(9)] #seno de solo los enteros
y = [fun(n) for n in range(9)]

plt.plot(x,y)
plt.xlabel('t')
plt.ylabel('seno(t)')

plt.title('grafica 1')

plt.show()