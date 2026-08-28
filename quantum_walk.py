import numpy as np
import matplotlib.pyplot as plt

num_steps = 50 
num_positions = 2 * num_steps + 1 
#iniial state of the photon, currently set to purely horizontal polarization (1H, 0V):
H_amplitudes = np.zeros(num_positions, dtype=complex)
V_amplitudes = np.zeros(num_positions, dtype=complex)

center = num_steps 

H_amplitudes[center] = 1.0  
V_amplitudes[center] = 0.0
#coin angle:
theta = np.pi / 8  

for step in range(num_steps):
    new_H = np.cos(2*theta) * H_amplitudes + np.sin(2*theta) * V_amplitudes
    new_V = np.sin(2*theta) * H_amplitudes - np.cos(2*theta) * V_amplitudes
    
    H_amplitudes = np.roll(new_H, 1)
    V_amplitudes = np.roll(new_V, -1)
#probabilty at each position:
probabilities = np.abs(H_amplitudes)**2 + np.abs(V_amplitudes)**2

positions = np.arange(-num_steps, num_steps + 1)
#plotting the graph:
plt.figure(figsize=(10, 6))
plt.bar(positions, probabilities, color='indigo', width=1.0)
plt.title(f"1D Coined Quantum Walk after {num_steps} Steps")
plt.xlabel("Position")
plt.ylabel("Probability")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
