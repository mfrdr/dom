#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:27:37 2024

@author: lucas
"""

import matplotlib.pyplot as plt

# Data
stations = ["308", "309", "310", "311", "312", "313", "316", "318", "319", "320", "321", "322", "323", "329", "332", "335", "337", "337"]
Surface = [301.7, 297.8, 289.7, 302.7, 262.4, 311.4, 280.6, 292.1, 296.2, 296, 277, 334.2, 313.9, 314.6, 325.8, 266.7, 273,0,0]
Bottom = [139.8, 145.2, 95.1, 128.7, 295.5, 259.1, 114.4, 173.8, 0, 106.5, 153.1, 215.6, 187.8, 136.5, 136.6, 0, 136.2,0,0]
Filteredbottom = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,349.4]
Filteredsurface = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,497.4]

# Filter data where both Surface and Bottom are not zero
stations_to_plot = []
Surface_to_plot = []
Filteredbottom_to_plot = []
Bottom_to_plot = []
Filteredsurface_to_plot = []
for i in range(len(stations)):
    if Surface[i] >= 0 or Bottom[i] >= 0:
        Surface_to_plot.append(Surface[i])
        Bottom_to_plot.append(Bottom[i])
        stations_to_plot.append(stations[i])
        Filteredbottom_to_plot.append(Filteredbottom[i])
        Filteredsurface_to_plot.append(Filteredsurface[i])
# Plotting
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size if needed
bar_width = 0.35
opacity = 0.8

# Plot bars
bar1 = ax.bar([i - bar_width/2 for i in range(1, len(stations_to_plot)+1)], Surface_to_plot, bar_width,
              alpha=opacity, color='tab:blue', label='Surface')
bar2 = ax.bar([i + bar_width/2 for i in range(1, len(stations_to_plot)+1)], Bottom_to_plot, bar_width,
              alpha=opacity, color='tab:orange', label='Bottom')
bar3=ax.bar([i - bar_width/2 for i in range(1, len(stations_to_plot)+1)], Filteredbottom_to_plot, bar_width,
              alpha=opacity, color='tab:purple',label="Bottom filtered")
bar4=ax.bar([i + bar_width/2 for i in range(1, len(stations_to_plot)+1)], Filteredsurface_to_plot, bar_width,
              alpha=opacity, color='tab:green',label="Surface filtered")
# Set x-axis ticks and labels
ax.set_xlabel('Stations',fontsize=18)
ax.set_ylabel('TOC [µM]',fontsize=18)
ax.set_title('Surface and Bottom TOC Across Stations',fontsize=22)
ax.set_xticks(range(1, len(stations_to_plot)+1))
ax.set_xticklabels(stations_to_plot)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)

ax.legend(fontsize=16)

plt.tight_layout()
plt.show()

#%%
import matplotlib.pyplot as plt

# Data
stations = ["308", "309", "310", "311", "312", "313", "316", "318", "319", "320", "321", "322", "323", "329", "332", "335", "337", "337"]
Surface = [15.7, 14, 14.6, 14.3, 15.6, 14.3, 15.8, 13.5, 15.6, 15.2, 15.7, 15.8, 14.7, 14.2, 14.3, 16.3, 18.3,0,0]
Bottom = [16.1, 15, 16.2, 16.6, 15.8, 16.1, 18.9, 15.6, 0, 17.4, 16.2, 16.5, 16.8, 18.4, 15.7, 17.8,0,0]
Filteredbottom = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31]
Filteredsurface = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25.6]

# Filter data where both Surface and Bottom are not zero
stations_to_plot = []
Surface_to_plot = []
Filteredbottom_to_plot = []
Bottom_to_plot = []
Filteredsurface_to_plot = []
for i in range(len(stations)):
    if Surface[i] >= 0 or Bottom[i] >= 0:
        Surface_to_plot.append(Surface[i])
        Bottom_to_plot.append(Bottom[i])
        stations_to_plot.append(stations[i])
        Filteredbottom_to_plot.append(Filteredbottom[i])
        Filteredsurface_to_plot.append(Filteredsurface[i])
# Plotting
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size if needed
bar_width = 0.35
opacity = 0.8

# Plot bars
bar1 = ax.bar([i - bar_width/2 for i in range(1, len(stations_to_plot)+1)], Surface_to_plot, bar_width,
              alpha=opacity, color='tab:blue', label='Surface')
bar2 = ax.bar([i + bar_width/2 for i in range(1, len(stations_to_plot)+1)], Bottom_to_plot, bar_width,
              alpha=opacity, color='tab:orange', label='Bottom')
bar3=ax.bar([i - bar_width/2 for i in range(1, len(stations_to_plot)+1)], Filteredbottom_to_plot, bar_width,
              alpha=opacity, color='tab:purple',label="Bottom filtered")
bar4=ax.bar([i + bar_width/2 for i in range(1, len(stations_to_plot)+1)], Filteredsurface_to_plot, bar_width,
              alpha=opacity, color='tab:green',label="Surface filtered")
# Set x-axis ticks and labels
ax.set_xlabel('Stations')
ax.set_ylabel('TN [µM]')
ax.set_title('Surface and Bottom TN Across Stations')
ax.set_xticks(range(1, len(stations_to_plot)+1))
ax.set_xticklabels(stations_to_plot)
ax.legend()

plt.tight_layout()
plt.show()








