import numpy as np 
import matplotlib.pyplot as plt
import scipy.io.wavfile 
import sounddevice

def sine(t, freq):
    return np.sin(2*np.pi*t*freq)

l_inf = 0
l_sup = 1

# sampling frequency
fs = 44100
no_samples = fs * (l_sup - l_inf)

r_continuous = np.linspace(start=l_inf, stop=l_sup, num=no_samples)

signal1 = sine(r_continuous, 400)
signal2 = sine(r_continuous, 800)

fig, axs = plt.subplots(2)
fig.suptitle("Sampled signals")

axs[0].plot(r_continuous[:500], signal1[:500])
axs[0].set_title("Sine signal freq 400")

axs[1].plot(r_continuous[:500], signal2[:500])
axs[1].set_title("Sine signal freq 800")

for ax in axs.flat:
    ax.set_xlim(l_inf,r_continuous[500])

plt.tight_layout()
plt.savefig("lab02/ex5/sine_signals.pdf")

plt.show()

appended_sine = np.append(signal1, signal2)
scipy.io.wavfile.write('lab02/ex5/appended_sine.wav', fs, appended_sine)

rate, x = scipy.io.wavfile.read('lab02/ex5/appended_sine.wav')
sounddevice.play(x, samplerate=fs)
sounddevice.wait()



