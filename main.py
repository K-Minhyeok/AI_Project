import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('temperature_data.csv', encoding='cp949')

years_summer = data.iloc[8:21, 0]
avg_temperatures = data.iloc[8:21, 2]  



plt.figure(figsize=(10, 6))
plt.plot(years_summer, avg_temperatures, marker='o', color='b', label='Average Temperature')
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.title('Average Temperature')
plt.legend()
plt.grid(True)
plt.show()
