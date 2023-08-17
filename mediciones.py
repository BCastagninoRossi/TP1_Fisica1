import numpy as np
import matplotlib.pyplot as plt


len1 = np.array([11.8, 6, 9.2, 6.8, 7.8, 7.7, 10.3, 13.9, 8.3, 11.2, 7.9, 15.8, 8.8, 6.1, 6.2, 7.2, 5.5, 5.2, 3.9, 10.8, 3.8, 10.7, 6.5, 4.9, 7])
len2 = np.array([12, 6.5, 9.2, 6.5, 7.7, 7.5, 10.5, 13.9, 8.3, 11.1, 7.9, 15.9, 8.8, 6.1, 6.4, 7.2, 5.5, 5.2, 4, 10.7, 3.3, 10.7, 6.3, 4.9, 7.5])
error = 0.5

wid1 = np.array([6.7, 6.1, 2.3, 5.7, 2.9, 7.5, 3.7, 5.8, 3.1, 6.8, 2.8, 7.7, 2.8, 3.8, 3.9, 3, 5.8, 2.6, 3.9, 4.8, 1.7, 6.8, 5.8, 3.5, 3.7])
wid2 = np.array([6.8, 6.2, 2.8, 5.7, 2.9, 7.5, 3.5, 5.3, 3, 6.8, 2.9, 7.6, 2.3, 3.9, 3.8, 2.9, 5.7, 2, 3.6, 4.2, 1.6, 6.9, 6, 3.3, 3.6])
error = 0.5

mass1 = np.array([1.19, 0.33, 0.26, 0.35, 0.45, 0.85, 0.43, 1.48, 0.28, 1.12, 0.18, 1.85, 0.21, 0.17, 0.44, 0.26, 0.33, 0.18, 0.10, 0.92, 0.10, 1.06, 0.39, 0.28, 0.33])
mass2 = np.array([1.15, 0.33, 0.21, 0.32, 0.43, 0.84, 0.4, 1.43, 0.21, 1.09, 0.15, 1.81, 0.19, 0.14, 0.42, 0.23, 0.32, 0.19, 0.9, 0.85, 0.08, 1.06, 0.39, 0.28, 0.34])
error = 0.005


len_avg = (len1 + len2) / 2
width_avg = (wid1 + wid2) / 2
mass_avg = (mass1 + mass2) / 2

area_17 = 0.25 * 85 #using squares
hojas_con_areas_romboidales = np.array([1, 3, 5, 13, 18, 22])


#Calculo de las areas
area = (len_avg /2) * (width_avg/2) * np.pi

for i in hojas_con_areas_romboidales:
    area[i] = (len_avg[i] * width_avg[i]) / 2

area_17 = 0.25 * 85 #using squares from papersheet
area[16] = area_17

#calculo del DS
sigma_len = np.std(len_avg)/5
sigma_width = np.std(width_avg)/5
sigma_area = np.sqrt(((0.25 * len_avg * np.pi)**2)*(sigma_len)**2   +   ((0.25* width_avg * np.pi)**2) *(sigma_width)**2)

mass_error_array = np.full(25, 0.005)
length_error_array = np.full(25, sigma_len)
width_error_array = np.full(25, sigma_width)

plt.figure(figsize=(8, 6))
plt.scatter(mass_avg, len_avg, c='blue', marker='o', label='Data Points')
plt.xlabel('Average Mass')
plt.ylabel('Length Average')
plt.title('Length vs. Mass')
plt.errorbar(x=mass_avg, y=len_avg, xerr=mass_error_array, yerr=length_error_array, fmt='none', ecolor='red', capsize=3, label='Error Bars')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(mass_avg, width_avg, c='blue', marker='o', label='Data Points')
plt.xlabel('Average Mass')
plt.ylabel('Width Average')
plt.title('Width vs. Mass')
plt.errorbar(x=mass_avg, y=width_avg, xerr=mass_error_array, yerr=length_error_array, fmt='none', ecolor='red', capsize=3, label='Error Bars')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(mass_avg, area, c='blue', marker='o', label='Data Points')
plt.xlabel('Average Mass')
plt.ylabel('Calculated Area')
plt.title('Area vs. Mass')
plt.errorbar(x=mass_avg, y=area, xerr=mass_error_array, yerr=sigma_area, fmt='none', ecolor='red', capsize=3, label='Error Bars')
plt.legend()
plt.grid(True)
plt.show()
