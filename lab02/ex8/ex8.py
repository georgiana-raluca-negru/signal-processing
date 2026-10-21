import numpy as np
import matplotlib.pyplot as plt

def pade_approximation(t):
    return (t-(7*(t**3))/60)/(1+(t**2)/20)

fs = 100
l_inf = -np.pi/2
l_sup = np.pi/2

r = np.arange(l_inf, l_sup, 1/fs)

fig, axs = plt.subplots(4)
fig.suptitle("Approximations for sine")

axs[0].plot(r, np.sin(r), color = "blue")
axs[0].plot(r, r, color = "red")
axs[0].set_title("Sine with Taylor approaximation")

axs[1].plot(r, np.sin(r), color = "blue")
axs[1].plot(r, pade_approximation(r), color = "red")
axs[1].set_title("Sine with Pade approximation")

axs[2].plot(r, np.abs(np.sin(r) - r))
axs[2].set_title("Absolute error with Taylor approximation")
axs[2].set_yscale('log')


axs[3].plot(r, np.abs(np.sin(r) - pade_approximation(r)))
axs[3].set_title("Absolute error with Pade approximation")
axs[3].set_yscale('log')


for ax in axs.flat:
    ax.set_xlim(l_inf,l_sup)

plt.tight_layout()
plt.savefig("lab02/ex8/sine_signals.pdf")

plt.show()
