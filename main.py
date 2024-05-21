import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv('\\temperature_data.csv', encoding='cp949')

years_summer = data.iloc[7:21, 0].astype(int).values.reshape(-1, 1)
avg_temperatures = pd.to_numeric(data.iloc[7:21, 2], errors='coerce').values

model = LinearRegression()
model.fit(years_summer, avg_temperatures)

future_years = np.array([2024, 2025, 2026, 2027, 2028, 2029, 2030]).reshape(-1, 1)
predicted_temperatures = model.predict(future_years)

plt.figure(figsize=(12, 6))
plt.plot(years_summer.flatten(), avg_temperatures, marker='o', color='b', label='Average Temperature')
plt.plot(future_years.flatten(), predicted_temperatures, marker='x', color='r', linestyle='--', label='Predicted Temperature')

plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Yearly Average Temperature of Summer')
plt.legend()
plt.grid(True)

plt.xticks(np.arange(min(years_summer), max(future_years)+1, 1))

plt.show()
