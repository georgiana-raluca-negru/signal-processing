import numpy as np
import matplotlib.pyplot as plt

def sine(t, freq):
    return np.sin(2*np.pi*t*freq + 0)

# sampling frequency
l_inf = 0
l_sup = 1
fs = 800

r_continuous = np.arange(l_inf, l_sup, 1/fs)

fig, axs = plt.subplots(3)
fig.suptitle("Sampled signals")

axs[0].plot(r_continuous[:100], sine(r_continuous, fs/2)[:100])
axs[0].set_title("Sine signal freq fs/2")

axs[1].plot(r_continuous[:100], sine(r_continuous, fs/4)[:100])
axs[1].set_title("Sine signal freq fs/4")

axs[2].plot(r_continuous[:100], sine(r_continuous, 0)[:100])
axs[2].set_title("Sine signal freq 0")

for ax in axs.flat:
    ax.set_xlim(l_inf,r_continuous[100])
    ax.set_ylim(-1, 1)

plt.tight_layout()
plt.savefig("lab02/ex6/sine_signals.pdf")

plt.show()
