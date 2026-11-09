import matplotlib.pyplot as plt
import numpy as np

def sine(t, f):
    return 1*np.sin(2*np.pi*t*f)

fs = 20
fs_vechi = 3

f0 = 2
f1 =  f0 + (-1)*fs_vechi
f2 =  f0 + 1*fs_vechi

t = np.arange(0, 1, 1/fs)
t_real = np.arange(0, 1, 1/1000)

fig, axs = plt.subplots(3, figsize=(8, 12))
fig.suptitle("Aliasing effect")

axs[0].plot(t_real, sine(t_real, f0), color = "blue")
axs[0].plot(t, sine(t, f0), 'ro', color = "yellow")
axs[1].plot(t_real, sine(t_real, f1), color = "purple")
axs[1].plot(t, sine(t, f1), 'ro', color = "yellow")
axs[2].plot(t_real, sine(t_real, f2), color = "green")
axs[2].plot(t, sine(t, f2), 'ro', color = "yellow")

plt.tight_layout()
plt.savefig("lab04/ex2/aliasing_effect.pdf")

plt.show()


