import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('california_cities.csv')
# data['area_total_km2'].sort_values(ascending=False)
# print(data.head())

# Extract latd = Vi do and Longd = Kinh do
lat, lon = data['latd'], data['longd']
population, area = data['population_total'], data['area_total_km2']

plt.figure(figsize=(8,6))
# Plot usign pytloy API
plt.scatter(lat, lon, c = np.log10(population), cmap='viridis', s=area, linewidths=0, alpha=0.5)
plt.xlabel('longtitude')
plt.ylabel('latitude')
plt.colorbar(label = 'log$_(10)$(population)')
plt.title('California Cities: population and area Distribution')

# vẽ chú thích kích cỡ từng thành phố
area_range = [50, 100, 300, 500]

for area in area_range:
    plt.scatter([],[], s=area, label=str(area) + 'km$^2')
    plt.legend(labelspacing=1, title='City area')

plt.savefig('cali_city.png')
plt.show()