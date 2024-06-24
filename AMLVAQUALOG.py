import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV files into dataframes
overall_data = pd.read_csv('OVERALL_DATA.csv', delimiter=";")
ctd_data = pd.read_csv('AML.csv', delimiter=";")

# Convert 'Depth' column to numeric
overall_data['Depth'] = pd.to_numeric(overall_data['Depth'].str.replace(',', '.'), errors='coerce')
overall_data['SensorValue'] = pd.to_numeric(overall_data['SensorValue'].str.replace(',', '.'), errors='coerce')

# Clean 'DOM' column in ctd_data
ctd_data['DOM'] = pd.to_numeric(ctd_data['DOM'].str.replace(',', '.'), errors='coerce')
ctd_data['Depth'] = pd.to_numeric(ctd_data['Depth'].str.replace(',', '.'), errors='coerce')

# Function to calculate average DOM within 1m of the specified depth
def calculate_dom_average(overall_data, ctd_data):
    results = []

    for index, row in overall_data.iterrows():
        station = row['Station']
        
        # Skip processing data for station 232
        if station == 232:
            continue
        
        sample_number = row['Sample']
        depth = row['Depth']
        
        # Filter CTD data for the same station
        ctd_station_data = ctd_data[ctd_data['Station'] == station]
        
        # Find the nearest depth in CTD data within 1 meter of the specified depth
        nearest_depth_index = ctd_station_data['Depth'].sub(depth).abs().idxmin()
        nearest_depth = ctd_station_data.loc[nearest_depth_index, 'Depth']
        
        # Calculate average DOM within 1 meter of the nearest depth
        dom_within_1m = ctd_station_data[(ctd_station_data['Depth'] >= nearest_depth - 1) & (ctd_station_data['Depth'] <= nearest_depth + 1)]
        
        # Check if dom_within_1m is not empty before calculating mean
        if not dom_within_1m.empty:
            average_dom = dom_within_1m['DOM'].mean()
        else:
            average_dom = None  # Handle case where no data is found
        
        # Determine if it's a surface or bottom sample
        sample_type = 'S' if 'S' in str(sample_number) else 'B' if 'B' in str(sample_number) else 'Unknown'
        
        results.append({
            'Station': station,
            'Sample': sample_number,
            'Depth': depth,
            'Sample_Type': sample_type,
            'Average_DOM': average_dom
        })
    
    return pd.DataFrame(results)

# Apply the function, excluding data from station 232
averages_df = calculate_dom_average(overall_data, ctd_data)

# Separate the results into surface and bottom samples
surface_samples = averages_df[averages_df['Sample_Type'] == 'S']
bottom_samples = averages_df[averages_df['Sample_Type'] == 'B']

# Output the results
print("Surface Samples:\n", surface_samples)
print("Bottom Samples:\n", bottom_samples)

# Convert pandas Series to numpy arrays for np.polyfit
x = overall_data['SensorValue'].to_numpy()
y = averages_df['Average_DOM'].to_numpy()

# Fit a linear regression line using np.polyfit
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, marker='o', c='blue', edgecolors='k', label='Samples')
plt.plot(x, p(x), color='red', label='Linear Fit')

# Print the linear equation on the plot
#plt.text(0.95, 0.1, f'Average_DOM = {z[0]:.2f} * SensorValue + {z[1]:.2f}', transform=plt.gca().transAxes, fontsize=12, ha='right', va='center', bbox=dict(facecolor='white', alpha=0.5))

plt.xlabel('SensorValue [Raman Units]',fontsize=18)
plt.ylabel('Average_DOM (AML) [Raman Units]',fontsize=16)
plt.title(f"Aqualog vs AML\nFit Equation: {p}",fontsize=16)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot to a file
plt.savefig('sensor_vs_average_dom_scatter.png')

# Show plot
plt.show()

# Calculate correlation between SensorValue and Average_DOM
correlation = overall_data['SensorValue'].corr(averages_df['Average_DOM'])
print(f"Correlation coefficient between SensorValue and Average_DOM: {correlation}")
