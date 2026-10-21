import numpy as np
import matplotlib.pyplot as plt

def sine(t, phase):
    return np.sin(2 * np.pi * t * 10 + phase)

def calculate_gamma(snr, x_norm, z_norm):
    return np.sqrt(x_norm**2/ (z_norm**2 * snr))

l_inf = 0
l_sup = 0.5
no_samples = 1000

r_continuous = np.linspace(start=l_inf, stop=l_sup, num=no_samples)

plt.plot(r_continuous, sine(r_continuous, np.pi/2))
plt.plot(r_continuous, sine(r_continuous, np.pi/3))
plt.plot(r_continuous, sine(r_continuous, np.pi/4))
plt.plot(r_continuous, sine(r_continuous, np.pi/6))

plt.title("Sine waves at different phases")
plt.savefig("lab02/ex2/phased_sine_waves.pdf")
plt.show()

x = sine(r_continuous, 0)
x_norm = np.linalg.norm(x)
z = np.random.normal(0, 1, size = len(x))
z_norm = np.linalg.norm(z)
snr_v = [0.1, 1.0, 10.0, 100.0]

fig, axs = plt.subplots(len(snr_v))
fig.suptitle("Signals with gaussian noise")

for i in range(len(snr_v)):
    gamma = calculate_gamma(snr=snr_v[i], x_norm=x_norm, z_norm=z_norm)
    new_signal = x + gamma * z

    axs[i].plot(r_continuous, new_signal, color="blue")
    axs[i].plot(r_continuous, x, color="red")

for ax in axs.flat:
    ax.set_xlim(l_inf,l_sup)

plt.tight_layout()
plt.savefig("lab02/ex2/noisy_signals.pdf")
plt.show()

