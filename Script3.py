import matplotlib.pyplot as plt
import numpy as np

# Valores de x en el rango deseado
x_values = np.linspace(-1.5,1.5, 400)

# Calculamos los valores correspondientes de y para cada valor de x
y_values = np.sqrt(1 - (x_values ** 2)) + (x_values ** 2) ** (1/3)
y_values_neg = -np.sqrt(1 - (x_values ** 2)) + (x_values ** 2) ** (1/3)

# Crear el grafico
plt.figure(figsize=(8,6))
plt.plot(x_values, y_values, label='Te')
plt.plot(x_values, y_values_neg, label = "Amo")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ecuacion del amor')
plt.legend()
plt.grid(True)
plt.show()
