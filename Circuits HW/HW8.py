import numpy as np
import matplotlib.pyplot as plt

# Time vector from 0 to 4 seconds (captures transients and steady state)
t = np.linspace(0, 4, 500)
omega_d = np.sqrt(91) / 2

# Calculate v_C(t)
v_C = 9 + np.exp(-1.5 * t) * (-9 * np.cos(omega_d * t) - (27 / np.sqrt(91)) * np.sin(omega_d * t))

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(t, v_C, label='$v_C(t)$', color='b', linewidth=2)
plt.axhline(9, color='r', linestyle='--', label='Steady-State Value ($9\text{ V}$)')
plt.title('Transient and Steady-State Response of $v_C(t)$')
plt.xlabel('Time $t$ (s)')
plt.ylabel('$v_C(t)$ (V)')
plt.grid(True)
plt.legend()
plt.show()