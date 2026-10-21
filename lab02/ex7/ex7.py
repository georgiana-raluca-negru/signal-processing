import numpy as np
import matplotlib.pyplot as plt

def sine(t):
    return np.sin(2*np.pi*t*10 + 0)

fs=1000
l_inf = 0
l_sup = 1

r = np.arange(l_inf, stop=l_sup, step=1/fs)
signal1 = sine(r)
signal2 = signal1[0::4]
signal3 = signal1[1::4]

fig, axs = plt.subplots(3)
fig.suptitle("Sampled signals")

axs[0].plot(r[:100], signal1[:100])
axs[0].set_title("Normal signal")

axs[1].plot(r[:25], signal2[:25])
axs[1].set_title("Derived signal 1")

axs[2].plot(r[:25], signal3[:25])
axs[2].set_title("Derived signal 2")

for ax in axs.flat:
    ax.set_xlim(l_inf,r[100])
    ax.set_ylim(-1, 1)

plt.tight_layout()
plt.savefig("lab02/ex7/sine_signals.pdf")

plt.show()
