import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Note:
# OVERALL_DATA.csv corresponds to DataCollection_m.xlsx
# ctd_data.csv corresponds to ctd_data.xlsx
overall_data = pd.read_csv('OVERALL_DATA.csv', delimiter=";")
ctd_data = pd.read_csv('ctd_data.csv', delimiter=";")

# Convert 'Depth' column to numeric
overall_data['Depth'] = pd.to_numeric(overall_data['Depth'].str.replace(',', '.'), errors='coerce')
overall_data['SensorValue'] = pd.to_numeric(overall_data['SensorValue'].str.replace(',', '.'), errors='coerce')

# Clean 'DOM' column in ctd_data
ctd_data['DOM'] = pd.to_numeric(ctd_data['DOM'].str.replace(',', '.'), errors='coerce')
ctd_data['Depth'] = pd.to_numeric(ctd_data['Depth'].str.replace(',', '.'), errors='coerce')

def calculate_dom_average(overall_data, ctd_data):
    results = []

    for index, row in overall_data.iterrows():
        station = row['Station']
        
        if station == 232:
            continue
        
        sample_number = row['Sample']
        depth = row['Depth']
        
        ctd_station_data = ctd_data[ctd_data['Station'] == station]
        
        nearest_depth_index = ctd_station_data['Depth'].sub(depth).abs().idxmin()
        nearest_depth = ctd_station_data.loc[nearest_depth_index, 'Depth']
        
        dom_within_1m = ctd_station_data[(ctd_station_data['Depth'] >= nearest_depth - 1) & (ctd_station_data['Depth'] <= nearest_depth + 1)]
        
        if not dom_within_1m.empty:
            average_dom = dom_within_1m['DOM'].mean()
        else:
            average_dom = None  # Handle case where no data is found
        
        sample_type = 'S' if 'S' in str(sample_number) else 'B' if 'B' in str(sample_number) else 'Unknown'
        
        results.append({
            'Station': station,
            'Sample': sample_number,
            'Depth': depth,
            'Sample_Type': sample_type,
            'Average_DOM': average_dom
        })
    
    return pd.DataFrame(results)

averages_df = calculate_dom_average(overall_data, ctd_data)

# Separate the results into surface and bottom samples
surface_samples = averages_df[averages_df['Sample_Type'] == 'S']
bottom_samples = averages_df[averages_df['Sample_Type'] == 'B']

print("Surface Samples:\n", surface_samples)
print("Bottom Samples:\n", bottom_samples)

# Results
x = overall_data['SensorValue'].to_numpy()
y = averages_df['Average_DOM'].to_numpy()

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, marker='o', c='blue', edgecolors='k', label='Samples')
plt.plot(x, p(x), color='red', label='Linear Fit')

plt.xlabel('SensorValue [Raman Units]',fontsize=18)
plt.ylabel('Average_DOM (AML) [Raman Units]',fontsize=16)
plt.title(f"Aqualog vs AML\nFit Equation: {p}",fontsize=16)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('sensor_vs_average_dom_scatter.png')
plt.show()

# Calculate correlation between SensorValue and Average_DOM
correlation = overall_data['SensorValue'].corr(averages_df['Average_DOM'])
print(f"Correlation coefficient between SensorValue and Average_DOM: {correlation}")
