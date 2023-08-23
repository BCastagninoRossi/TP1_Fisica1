import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

len = np.array([8, 10, 12, 18, 22, 24, 27])
masa = np.array([0.51, 0.82, 1.16, 2.64, 3.98, 4.69, 6.17])
diam = np.array([1.3, 1.6, 1.8, 2.6, 3.1, 3.3, 3.5])

plt.scatter(masa, len, label="Mediciones")
plt.xlabel('Masa (gr)', fontsize=13)
plt.ylabel('Longitud (cm)', fontsize=13)
plt.title('Longitud vs. masa', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()

plt.scatter(masa, diam, label="Mediciones")
plt.xlabel('Masa (gr)', fontsize=13)
plt.ylabel('Diámetro (cm)', fontsize=13)
plt.title('Diametro vs. masa', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()

# -------------------------- LEY DE ESCALA ---------------------------------
x = masa
y = diam
y_err =  np.full(7, 0.05)

def power_law(x, a, b):
    return a *pow(x, b)

def linear_model(x, m, c):
    return m * x + c

log_x = np.log10(x)
log_y = np.log10(y)
log_y_err = y_err / (y * np.log(10))

popt_linear, pcov_linear = curve_fit(linear_model, log_x, log_y, sigma=log_y_err, absolute_sigma=True)
m, c = popt_linear
m_err, c_err = np.sqrt(np.diag(pcov_linear))

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 2)
plt.errorbar(log_x, log_y, yerr=log_y_err, fmt='o', label="Incerteza")
plt.plot(log_x, linear_model(log_x, m, c), label=f"Ajuste: y={m:.2f}±{m_err:.2f}x + {c:.2f}±{c_err:.2f}")
plt.xlabel("log(masa)")
plt.ylabel("log(diámetro)")
plt.legend()
plt.title("Muestras en Log-Log con ajuste lineal")
plt.tight_layout()
plt.show()

x_fit = np.linspace(min(x), max(x), 400)
ordenada = pow(10, c)
# Graficamos con barras de error
plt.errorbar(x, y, yerr=y_err, fmt='o', label="Muestras")
plt.plot(x_fit, power_law(x_fit, ordenada, m), label=f"Ajuste: y={ordenada:.2f}x^{m:.2f}")
plt.xlabel("Masa (gr)")
plt.ylabel("Diámetro (cm)")
plt.legend()
plt.title("Muestras ajustadas con la Ley de potencias")
plt.show()

y_pred = power_law(x, ordenada, m)
relative_error = np.sum((y-y_pred)**2)/np.sum(y**2)
print("Error relativo acumulado (largo vs masa): ", relative_error)

# Es importante analizar los coeficientes junto a sus incertezas asociadas
print(f"Pendiente (m): {m:.2f} ± {m_err:.2f}")
print(f"Ordenada al origen (c): {c:.2f} ± {c_err:.2f}")

