import matplotlib.pyplot as plt
import numpy as np

# 2pi*260t + pi/3
# frequency of signal 260 (260 full circles in a second)
def x_function(t):
    return np.cos(520*np.pi*t + np.pi/3)

# 2pi*140t + pi/3
# frequency of signal 140 (140 full circles in a second)
def y_function(t):
    return np.cos(280*np.pi*t - np.pi/3)

# 2pi*60*t+ pi/3
# frequency of signal 60 (60 full circles in a second)
def z_function(t):
    return np.cos(120*np.pi*t + np.pi/3)

# Number of functions and respectively subplots
no_functions = 3
# Inferior limit of the interval (in seconds)
l_inf = 0
# Superior limit of the interval (in seconds)
l_sup = 0.03
step_continuous = 0.0005
# Sampling frequency
freq = 200

# a)
r_continuous = np.linspace(start=l_inf, stop=l_sup, num=int((l_sup-l_inf)/step_continuous))
r_sampled = np.linspace(start=l_inf, stop=l_sup, num=int((l_sup-l_inf)*freq))

fig, axs = plt.subplots(no_functions)
fig.suptitle("Sampled signals")

axs[0].stem(r_sampled, x_function(r_sampled))
axs[0].plot(r_continuous, x_function(r_continuous))
axs[0].set_title("X")

axs[1].stem(r_sampled, y_function(r_sampled))
axs[1].plot(r_continuous, y_function(r_continuous))
axs[1].set_title("Y")

axs[2].stem(r_sampled, z_function(r_sampled))
axs[2].plot(r_continuous, z_function(r_continuous))
axs[2].set_title("Z")

for ax in axs.flat:
    ax.set_xlim(l_inf,l_sup)

plt.savefig("lab01/Sampled_signals_ex1.pdf")

plt.show()
