import streamlit as st
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

st.header("Introduction", divider='rainbow')
st.write(
    "Hallo, Wellcome to my personal website, hehe"
)




#hari pertama solstis
N = 171
om = 2*math.pi/365.24 #kecepatan sudut dalam radian/hari
ecl = math.radians(23.44) #kemiringan ekliptika

#persamaan deklinasi Matahari
delta = -math.asin(math.sin(ecl)*math.cos(om*(N+10)))
print("deklinasi: ", math.degrees(delta))

plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['axes.titlesize'] = 20

N = np.arange(1, 365, 1)
dp = []

for i in N:
    delta = -math.asin(math.sin(ecl)*math.cos(om*(i+10)))
    dp.append(math.degrees(delta))

plt.figure(figsize=(10, 5))

plt.title(r"Variasi Deklinasi Matahari $\delta_\odot$", pad=20)
plt.plot(N, dp)

#equator
plt.axhline(y=0, color='black', linestyle='--')
plt.text(367, 0, 'Ekuator', va='center', ha='left', fontsize=12)

#tropic of cancer
plt.axhline(y=23.44, color='black', linestyle='--')
plt.text(367, 23.44, 'Garis Balik Utara \nTropic of Cancer', va='center', ha='left', fontsize=12)

#tropic of capricorn
plt.axhline(y=-23.44, color='black', linestyle='--')
plt.text(367, -23.44, 'Garis Balik Selatan \nTropic of Capricorn', va='center', ha='left', fontsize=12)

#limit plotting
plt.xlim(0, 365)
plt.ylim(-25, 25)

#nilai maksimum
max = np.argmax(dp)
plt.scatter(N[max], dp[max], color='red', label='Maxima')
#plt.text(N[max], dp[max], 'Solstis Juni', fontsize=10, va='center', ha='left', color='red')

#nilai minimum
min = np.argmin(dp)
plt.scatter(N[min], dp[min], color='blue', label='Minima')
#plt.text(N[min], dp[min], 'Solstis Desember', fontsize=10, va='c enter', ha='left', color='blue')

#menambahkan waktu ekuinoks dan solstis
plt.axvline(x=81, color='black', linestyle=':')
plt.axvspan(0, 81, facecolor='blue', alpha=0.2)
plt.axvspan(356, 365, facecolor='blue', alpha=0.2)
plt.axvline(x=173, color='black', linestyle=':')
plt.axvspan(82, 173, facecolor='green', alpha=0.2)
plt.axvline(x=264, color='black', linestyle=':')
plt.axvspan(174, 264, facecolor='yellow', alpha=0.2)
plt.axvline(x=355, color='black', linestyle=':')
plt.axvspan(265, 355, facecolor='peru', alpha=0.4)

#teks
plt.text(43, -32, 'Musim Dingin', ha='center', fontsize=12, color='blue')
plt.text(129, -32, 'Musim Semi', ha='center', fontsize=12, color='g')
plt.text(219, -32, 'Musim Panas', ha='center', fontsize=12, color='orange')
plt.text(310, -32, 'Musim Gugur', ha='center', fontsize=12, color='peru')

# Ubah label sumbu x menjadi bulan
month_ticks = np.arange(15, 365, 30)  # Kira-kira setiap 30 hari
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
plt.xticks(month_ticks, month_labels)

plt.minorticks_on()

plt.ylabel(r"Deklinasi ($\degree$)")

plt.show()
