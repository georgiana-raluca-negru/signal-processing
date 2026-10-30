import math
import numpy as np
import matplotlib.pyplot as plt

# number of fourier components
n = 8

F = np.zeros((n, n), dtype=complex)

for k in range(n):
    for m in range(n):
        F[k, m] = np.cos((-2*np.pi*k*m)/n) - (np.sin((-2*np.pi*k*m)/n))*1j

F_H = (np.conj(F)).T
identity_multiple = n * np.eye(n)

is_unitary = np.allclose(np.matmul(F_H, F), identity_multiple)
print(f"Matricea Fourier F este unitara? {"Da" if is_unitary else "Nu"}")

fig, axs = plt.subplots(n, figsize=(8, 12))
fig.suptitle("Fourier components")

for i, ax  in enumerate(axs.flat):
    ax.plot(np.real(F[i, :]), color = "red", label = "Real")
    ax.plot(np.imag(F[i, :]), color = "blue", label = "Imaginary")
    ax.set_title(f"{i+1} fourier component")

plt.tight_layout()
plt.savefig("lab03/ex1/fourier_componennts.pdf")

plt.show()

