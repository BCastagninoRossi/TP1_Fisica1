import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
 
len1 = np.array([11.8, 6, 9.2, 6.8, 7.8, 7.7, 10.3, 13.9, 8.3, 11.2, 7.9, 15.8, 8.8, 6.1, 6.2, 7.2, 5.5, 5.2, 3.9, 10.8, 3.8, 10.7, 6.5, 4.9, 7])
len2 = np.array([12, 6.5, 9.2, 6.5, 7.7, 7.5, 10.5, 13.9, 8.3, 11.1, 7.9, 15.9, 8.8, 6.1, 6.4, 7.2, 5.5, 5.2, 4, 10.7, 3.3, 10.7, 6.3, 4.9, 7.5])
error = 0.5

wid1 = np.array([6.7, 6.1, 2.3, 5.7, 2.9, 7.5, 3.7, 5.8, 3.1, 6.8, 2.8, 7.7, 2.8, 3.8, 3.9, 3, 5.8, 2.6, 3.9, 4.8, 1.7, 6.8, 5.8, 3.5, 3.7])
wid2 = np.array([6.8, 6.2, 2.8, 5.7, 2.9, 7.5, 3.5, 5.3, 3, 6.8, 2.9, 7.6, 2.3, 3.9, 3.8, 2.9, 5.7, 2, 3.6, 4.2, 1.6, 6.9, 6, 3.3, 3.6])
error = 0.5

mass1 = np.array([1.19, 0.33, 0.26, 0.35, 0.45, 0.85, 0.43, 1.48, 0.28, 1.12, 0.18, 1.85, 0.21, 0.17, 0.44, 0.26, 0.33, 0.18, 0.10, 0.92, 0.10, 1.06, 0.39, 0.28, 0.33])
mass2 = np.array([1.15, 0.33, 0.21, 0.32, 0.43, 0.84, 0.4, 1.43, 0.21, 1.09, 0.15, 1.81, 0.19, 0.14, 0.42, 0.23, 0.32, 0.19, 0.9, 0.85, 0.08, 1.06, 0.39, 0.28, 0.34])
error = 0.01


len_avg = (len1 + len2) / 2
width_avg = (wid1 + wid2) / 2
mass_avg = (mass1 + mass2) / 2

#Areas with ellipses
area = (len_avg /2) * (width_avg/2) * np.pi

#used squares to calculate the area of leaf n°17
area_17 = 0.25 * 85 
area[16] = area_17

#We will use rombuses to calculate the areas of this leaves 
romb_areas = np.array([1, 3, 5, 13, 18, 22]) 
for i in romb_areas:
    area[i] = (len_avg[i] * width_avg[i]) / 2

#calculation of standard deviations
sigma_len = np.std(len_avg)/5
sigma_width = np.std(width_avg)/5
sigma_area = np.sqrt(((0.25 * len_avg * np.pi)**2)*(sigma_len)**2   +   ((0.25* width_avg * np.pi)**2) *(sigma_width)**2)

mass_error_array = np.full(25, 0.01)
length_error_array = np.full(25, 0.5)
width_error_array = np.full(25, 0.5)

# Función para ajustar
def func(params, x):
    a, b = params
    return a * x + b

# Función de error
def error_func(params, x, y):
    return func(params, x) - y

def plot_len_mass(mass_avg, len_avg, mass_error_array, length_error_array):
    initial_params = [1.0, 0.0]

    # Ajuste por mínimos cuadrados usando least_squares
    result = least_squares(error_func, initial_params, args=(mass_avg, len_avg))

    # Parámetros ajustados
    a, b = result.x

    # Valores predichos
    y_pred = func(result.x, mass_avg)

    # Gráfica de los datos y el ajuste
    plt.scatter(mass_avg, len_avg, label='Mediciones')
    plt.plot(mass_avg, y_pred, color='green', label=f'Ajuste: $y = {a:.2f}x + {b:.2f}$')
    plt.xlabel('Masa (gr)', fontsize=13)
    plt.ylabel('Longitud (cm)', fontsize=13)
    plt.title('Longitud vs. masa', fontsize=14)
    plt.errorbar(x=mass_avg, y=len_avg, xerr=mass_error_array, yerr=length_error_array, fmt='none', ecolor='red', capsize=3, label='Incerteza')
    plt.legend()
    plt.grid(True)
    plt.show()

    relative_error = np.sum((len_avg-y_pred)**2)/np.sum(len_avg**2)
    print("Error relativo acumulado (largo vs masa): ", relative_error)


def plot_width_mass(width_avg, mass_avg, mass_error_array, width_error_array):
    initial_params = [1.0, 0.0]

    # Ajuste por mínimos cuadrados usando least_squares
    result = least_squares(error_func, initial_params, args=(mass_avg, width_avg))

    # Parámetros ajustados
    a, b = result.x

    # Valores predichos
    y_pred = func(result.x, mass_avg)

    # Gráfica de los datos y el ajuste
    plt.scatter(mass_avg, width_avg, label='Mediciones')
    plt.plot(mass_avg, y_pred, color='green', label=f'Ajuste: $y = {a:.2f}x + {b:.2f}$')
    plt.xlabel('Masa (gr)', fontsize=13)
    plt.ylabel('Ancho (cm)', fontsize=13)
    plt.title('Ancho vs. masa', fontsize=14)
    plt.errorbar(x=mass_avg, y=width_avg, xerr=mass_error_array, yerr=width_error_array, fmt='none', ecolor='red', capsize=3, label='Incerteza')
    plt.legend()
    plt.grid(True)
    plt.show()

    relative_error = np.sum((width_avg-y_pred)**2)/np.sum(width_avg**2)
    print("Error relativo acumulado (ancho vs masa): ", relative_error)


def plot_area_mass(area, mass_avg, mass_error_array, sigma_area):
    initial_params = [1.0, 0.0]

    # Ajuste por mínimos cuadrados usando least_squares
    result = least_squares(error_func, initial_params, args=(mass_avg, area))

    # Parámetros ajustados
    a, b = result.x

    # Valores predichos
    y_pred = func(result.x, mass_avg)

    # Gráfica de los datos y el ajuste
    plt.scatter(mass_avg, area, label='Mediciones')
    plt.plot(mass_avg, y_pred, color='green', label=f'Ajuste: $y = {a:.2f}x + {b:.2f}$')
    plt.xlabel('Masa (gr)', fontsize=13)
    plt.ylabel('Área (cm^2)', fontsize=13)
    plt.title('Área vs. masa', fontsize=14)
    plt.errorbar(x=mass_avg, y=area, xerr=mass_error_array, yerr=sigma_area, fmt='none', ecolor='red', capsize=3, label='Incerteza')
    plt.legend()
    plt.grid(True)
    plt.show()


    relative_error = np.sum((area-y_pred)**2)/np.sum(area**2)
    print("Error relativo acumulado (area vs masa): ", relative_error)

#plot_len_mass(mass_avg, len_avg, mass_error_array, length_error_array)
#plot_width_mass(width_avg, mass_avg, mass_error_array, width_error_array)
#plot_area_mass(area, mass_avg, mass_error_array, sigma_area)
