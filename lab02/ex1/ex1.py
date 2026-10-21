import numpy as np
import matplotlib.pyplot as plt 

class Functions:
    def __init__(self):
        self.A = 1
        self.freq = 60
        self.phase = np.pi/3

    def sine(self, t):
        return self.A * np.sin(2 * np.pi * self.freq * t + self.phase)

    def cosine(self, t):
        return self.A * np.cos(2 * np.pi * self.freq * t + self.phase - np.pi/2)


f = Functions()

l_inf = 0
l_sup = 0.2
no_samples = 1000

r_continuous = np.linspace(start = l_inf, stop = l_sup, num = no_samples )

fig, axs = plt.subplots(2)
fig.suptitle("Sine & Cosine")

axs[0].plot(r_continuous, f.sine(r_continuous))
axs[0].set_title("Sine")

axs[1].plot(r_continuous, f.cosine(r_continuous))
axs[1].set_title("Cosine")

for ax in axs.flat:
    ax.set_xlim(l_inf,l_sup)

plt.tight_layout()
plt.savefig("lab02/ex1/identical_sine_cosine.pdf")

plt.show()