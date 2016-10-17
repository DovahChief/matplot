import matplotlib.pyplot as plt
import math

def fun(x):     #funcion seno
    return math.sin(x)

x = [n for n in range(9)] #seno de solo los enteros
y = [fun(n) for n in range(9)]

x2 = [n+0.5 for n in range(9)] #seno de solo los enteros
y2 = [fun(n+0.5) for n in range(9)]

plt.plot(x,y , label ='orig')
plt.plot(x2,y2 , label = 'seg')

plt.legend()

plt.xlabel('tiempo (t)')
plt.ylabel('seno(t)')

plt.title('grafica 1 \nmatplotlib')

plt.show()