import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('temperature_data.csv', encoding='cp949')

years_summer = data.iloc[7:21, 0]
avg_temperatures = data.iloc[7:21, 2]
avg_temperatures = pd.to_numeric(avg_temperatures, errors='coerce')


plt.figure(figsize=(10, 6))
plt.plot(years_summer, avg_temperatures, marker='o', color='b', label='Average Temperature')
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Yearly Average Temperature of Summer')
plt.legend()
plt.grid(True)
plt.show()
