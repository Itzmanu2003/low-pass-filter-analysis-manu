# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 09:43:45 2025

@author: MANU K
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Given Data ---
frequency = np.array([100, 500, 1000, 2000, 5000, 10000])   # in Hz
vin = np.array([2, 2, 2, 2, 2, 2])                         # Input voltage (V)
vout = np.array([0.65, 0.095, 0.036, 0.0037, 0.011, 0.0035]) # Output voltage (V)

# --- Gain Calculation ---
gain_db = 20 * np.log10(vout / vin)  # Gain in decibels (dB)

# --- Display data (optional) ---
print("Frequency (Hz)\tGain (dB)")
for f, g in zip(frequency, gain_db):
    print(f"{f}\t\t{g:.2f}")

# --- Plot ---
plt.figure(figsize=(8,5))
plt.semilogx(frequency, gain_db, 'o-', color='orange', linewidth=2, markersize=6)
plt.title("Gain vs Frequency (RC Low Pass Filter)", fontsize=14)
plt.xlabel("Frequency (Hz)", fontsize=12)
plt.ylabel("Gain (dB)", fontsize=12)
plt.grid(True, which="both", linestyle="--", linewidth=0.7)

# --- Optional: Highlight Cutoff Frequency (-3 dB point) ---
# find closest value to -3 dB
cutoff_index = np.argmin(np.abs(gain_db + 3))
plt.scatter(frequency[cutoff_index], gain_db[cutoff_index], color='red')
plt.legend()

plt.show()