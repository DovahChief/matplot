import matplotlib.pyplot as plt
import math


x = [n for n in range(9) if n%2 == 0] #seno de solo los enteros
y = [10,12,3,12, 9]

x2 = [n for n in range(9) if n%2 != 0] #seno de solo los enteros
y2 = [15,12,13,20]

plt.bar(x,y , label ='pares' , color = 'g')
plt.bar(x2,y2 , label = 'impares')

plt.legend()

plt.xlabel('mes')
plt.ylabel('chocolates')

plt.title('grafica 1 \nmatplotlib')

plt.show()