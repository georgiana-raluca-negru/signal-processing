import matplotlib.pylab as plt
import numpy as np
import math

# custom signal (10hz, 20hz and 60hz components)
def custom_signal(t):
    return np.sin(2*np.pi*t*10) + np.sin(2*np.pi*20*t) + np.sin(2*np.pi*t*60)

l_inf = 0
l_sup = 1
fs = 1000
r = np.arange(l_inf, stop=l_sup, step=1/fs)

omegas = [ x for x in range(1, 101)]
x = custom_signal(r)

fourier_values = []

for w in omegas:
    # X(w) = sum(x(t)*e^(-2pi*j*w*t))
    fourier_val = np.sum(x*(math.e**(-2j*np.pi*r*w)))
    fourier_values.append(np.abs(fourier_val))


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

ax1.plot(r, x)
ax1.set_title("Custom Signal")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")
# horizontal axis
ax1.axhline(0, color='grey', linestyle='--', linewidth=0.5) 
# vertical axis
ax1.axvline(0, color='grey', linestyle='--', linewidth=0.5) 

ax2.plot(omegas, fourier_values, color = "indigo")
ax2.set_title("Absolute value of the fourier transform")
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Value")
# horizontal axis
ax2.axhline(0, color='grey', linestyle='--', linewidth=0.5) 
# vertical axis
ax2.axvline(0, color='grey', linestyle='--', linewidth=0.5) 

plt.savefig("lab03/ex3/fourier_transform.pdf")
plt.show()
