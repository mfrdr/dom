import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Function to read and clean CSV data
def read_csv(file_path):
    df = pd.read_csv(file_path, delimiter=';')
    return df

# Path to your CSV file
file_path = 'FDOM2.csv'

# Read the CSV file
df = read_csv(file_path)

# Convert columns to numeric
df["TOC"] = pd.to_numeric(df["TOC"], errors='coerce')
df["T"] = pd.to_numeric(df["T"], errors='coerce')
df["A"] = pd.to_numeric(df["A"], errors='coerce')
df["M"] = pd.to_numeric(df["M"], errors='coerce')
df["C"] = pd.to_numeric(df["C"], errors='coerce')
df["D"] = pd.to_numeric(df["D"], errors='coerce')
df["N"] = pd.to_numeric(df["N"], errors='coerce')

# List of parameters to plot
parameters = ["T", "A", "M", "C", "D", "N"]

# Create a figure with subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 12))

# Flatten the axs array for easier iteration
axs = axs.flatten()

# Iterate over each parameter
for i, param in enumerate(parameters):
    # Extract data
    y = df["TOC"].to_numpy()
    x = df[param].to_numpy()

    # Calculate linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    # Calculate R-squared
    r_squared = r_value ** 2
    rounded_r = round(r_squared, 2)
    print(f"R-squared value for {param}: {r_squared}")
    # Scatter plot
    axs[i].scatter(x, y)

    # Add regression line
    axs[i].plot(x, intercept + slope * x, color='red')

    # Add labels and title
    axs[i].set_xlabel(f"{param} [Raman Units]")
    axs[i].set_ylabel("TOC [μM]")
    axs[i].set_title(f"{param} vs TOC ($R^2$={rounded_r})")
    axs[i].grid(True)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
#%%
correlation = df["TOC"].corr(df["T"])
print(f"CORR T= {correlation}")
correlation = df["TOC"].corr(df["A"])
print(f"CORR A= {correlation}")
correlation = df["TOC"].corr(df["M"])
print(f"CORR M= {correlation}")
correlation = df["TOC"].corr(df["C"])
print(f"CORR C= {correlation}")
correlation = df["TOC"].corr(df["D"])
print(f"CORR D= {correlation}")
correlation = df["TOC"].corr(df["N"])
print(f"CORR N= {correlation}")









