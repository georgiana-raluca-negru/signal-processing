import time
import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    n = len(x)

    if n == 1:
        return x
    
    # separating the samples between even and odd
    even, odd = x[0::2], x[1::2]
    y_even = fft(even)
    y_odd = fft(odd)

    y = [0]*n

    for j in range(n//2):
        # the different roots of unit, wrapping around the circle, but only half of them 
        # because the other diametral point omega(j+n/2) = -omega(j)
        omega = np.exp(-2j*np.pi*j/n)
        y[j] = y_even[j] + omega*y_odd[j]
        # for the other half
        y[j + n//2] = y_even[j] - omega*y_odd[j]

    # y will hold the fourier components 
    return  np.array(y)


# number of fourier components
n_values = [128, 256, 512, 1024, 2048, 4096, 8192]

# array for keeping track of the time for each of the n values  
times_fft_np = []
times_fft_custom = []

for n in n_values:

    x = np.random.rand(n)
    start = time.perf_counter()
    fft(x)
    end = time.perf_counter()
    times_fft_custom.append(end-start)

    # ======================================================================

    start = time.perf_counter()
    np.fft.fft(x)
    end = time.perf_counter()
    times_fft_np.append(end-start)
    

plt.figure(figsize=(10, 6))

plt.plot(n_values, times_fft_custom, marker='s', label='Custom FFT')
plt.plot(n_values, times_fft_np, marker='^', label='NumPy FFT')

plt.yscale('log')
plt.xscale('log', base=2) 
plt.xticks(n_values, labels=[str(val) for val in n_values])

plt.xlabel('Dimensiunea Matricii (N x N)')
plt.ylabel('Log(Time)')
plt.title('Time comparison')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)

plt.tight_layout()
plt.savefig("lab04/ex1/compare_time.pdf")
plt.show()
