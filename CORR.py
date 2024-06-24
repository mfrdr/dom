import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def read_csv(file_path):
    df = pd.read_csv(file_path, delimiter=';')
    return df
 
file_path = 'Raw/FDOM2.csv'

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

parameters = ["T", "A", "M", "C", "D", "N"]

# Results
fig, axs = plt.subplots(3, 2, figsize=(12, 12))
axs = axs.flatten()

for i, param in enumerate(parameters):
    y = df["TOC"].to_numpy()
    x = df[param].to_numpy()

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    r_squared = r_value ** 2
    rounded_r = round(r_squared, 2)
    print(f"R-squared value for {param}: {r_squared}")

    axs[i].scatter(x, y)
    axs[i].plot(x, intercept + slope * x, color='red')
    axs[i].set_xlabel(f"{param} [Raman Units]")
    axs[i].set_ylabel("TOC [μM]")
    axs[i].set_title(f"{param} vs TOC ($R^2$={rounded_r})")
    axs[i].grid(True)

plt.tight_layout()

plt.show()

#Correlations
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









