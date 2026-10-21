import numpy as np
import matplotlib.pyplot as plt

# 6 full circles per second
def sine(t):
    return np.sin(2*np.pi*6*t)

# 6 teeth per second
def sawtooth(t):
    return np.mod(t*6, 1)

l_inf = 0
l_sup = 1
no_samples = 20*6

r_continuous = np.linspace(start=l_inf, stop=l_sup, num=no_samples)

fig, axs = plt.subplots(3)
fig.suptitle("Sampled signals")

axs[0].plot(r_continuous, sine(r_continuous))
axs[0].stem(r_continuous, sine(r_continuous))
axs[0].set_title("Sine signal")

axs[1].plot(r_continuous, sawtooth(r_continuous))
axs[1].stem(r_continuous, sawtooth(r_continuous))
axs[1].set_title("Sawtooth signal")

axs[2].plot(r_continuous, sine(r_continuous) + sawtooth(r_continuous))
axs[2].stem(r_continuous, sine(r_continuous) + sawtooth(r_continuous))
axs[2].set_title("SUm of signals")

for ax in axs.flat:
    ax.set_xlim(l_inf,l_sup)

plt.tight_layout()
plt.savefig("lab02/ex4/sine_sawtooth.pdf")

plt.show()