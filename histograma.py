import matplotlib.pyplot as plt

edades_p = [23,43,55,46,32,123,57,89,90,22,76,64,88]
bins = [n for n in range(130) if n%10 == 0]

plt.hist(edades_p, bins , histtype = 'bar', rwidth = 0.8 , label  ='e')

plt.xlabel('edades')
plt.ylabel('poblacion')

plt.title('histograma de edades')
plt.legend()
plt.show()