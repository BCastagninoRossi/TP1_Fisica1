import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos de prueba
x = np.array([1.19, 0.33, 0.26, 0.35, 0.45, 0.85, 0.43, 1.48, 0.28, 1.12, 0.18, 1.85, 0.21, 0.17, 0.44, 0.26, 0.33, 0.18, 0.10, 0.92, 0.10, 1.06, 0.39, 0.28, 0.33])
#y = np.array([6.7, 6.1, 2.3, 5.7, 2.9, 7.5, 3.7, 5.8, 3.1, 6.8, 2.8, 7.7, 2.8, 3.8, 3.9, 3, 5.8, 2.6, 3.9, 4.8, 1.7, 6.8, 5.8, 3.5, 3.7])
y = np.array([11.8, 6, 9.2, 6.8, 7.8, 7.7, 10.3, 13.9, 8.3, 11.2, 7.9, 15.8, 8.8, 6.1, 6.2, 7.2, 5.5, 5.2, 3.9, 10.8, 3.8, 10.7, 6.5, 4.9, 7])

# Error asociado a la variable y (esto es inventado, ustedes ponen los que midieron o calcularon)
y_err =  np.full(25, 0.5)

# Definimos una ley de escala para el ajuste
def power_law(x, a, b):
    return a *pow(x, b)

# Hacemos cuadrados mínimos pesados con los errores de y usando curve_fit
popt, pcov = curve_fit(power_law, x, y, sigma=y_err, absolute_sigma=True)
a, b = popt

x_fit = np.linspace(min(x), max(x), 400)

# Graficamos con barras de error
plt.errorbar(x, y, yerr=y_err, fmt='o', label="Data")
plt.plot(x_fit, power_law(x_fit, a, b), label=f"Fit: y={a:.2f}x^{b:.2f}")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Data como ley de potencias")
plt.show()

# PARTE DOS ---------------------------------

# Modelo linear con la data en log-log
def linear_model(x, m, c):
    return m * x + c

# Hacemos el logaritmo de los datos
log_x = np.log10(x)
log_y = np.log10(y)
log_y_err = y_err / (y * np.log(10))

# Para que log_y_err no tenga valores negativos, los paso como errores absolutos
popt_linear, pcov_linear = curve_fit(linear_model, log_x, log_y, sigma=log_y_err, absolute_sigma=True)
m, c = popt_linear
m_err, c_err = np.sqrt(np.diag(pcov_linear))

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 2)
plt.errorbar(log_x, log_y, yerr=log_y_err, fmt='o', label="Incerteza")
plt.plot(log_x, linear_model(log_x, m, c), label=f"Ajuste: y={m:.2f}±{m_err:.2f}x + {c:.2f}±{c_err:.2f}")
plt.xlabel("log(masa)")
plt.ylabel("log(ancho)")
plt.legend()
plt.title("Muestras en Log-Log con ajuste lineal")

"""
plt.subplot(1, 2, 1)
plt.errorbar(x, y, yerr=y_err, fmt='o', label="Data")
plt.plot(x, power_law(x, a, m), label=f"Power Law Fit: y={a:.2f}x^{b:.2f}")
plt.plot(x_fit, power_law(x_fit, a, b), label=f"Fit: y={a:.2f}x^{b:.2f}") #Lo agregue yo
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Data con ajuste de ley de potencias")
"""

plt.tight_layout()
plt.show()

#--------- AGREGADO POR Mí -----------------
x_fit = np.linspace(min(x), max(x), 400)
ordenada = pow(10, c)
# Graficamos con barras de error
plt.errorbar(x, y, yerr=y_err, fmt='o', label="Muestras")
plt.plot(x_fit, power_law(x_fit, ordenada, m), label=f"Ajuste: y={ordenada:.2f}x^{m:.2f}")
plt.xlabel("Masa (gr)")
plt.ylabel("Ancho (cm)")
plt.legend()
plt.title("Muestras ajustadas con la Ley de potencias")
plt.show()

y_pred = power_law(x, ordenada, m)
relative_error = np.sum((y-y_pred)**2)/np.sum(y**2)
print("Error relativo acumulado (largo vs masa): ", relative_error)

# Es importante analizar los coeficientes junto a sus incertezas asociadas
print(f"Pendiente (m): {m:.2f} ± {m_err:.2f}")
print(f"Ordenada al origen (c): {c:.2f} ± {c_err:.2f}")