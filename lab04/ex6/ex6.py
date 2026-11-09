import matplotlib.pyplot as plt
import scipy.io.wavfile
import numpy as np

fs, signal = scipy.io.wavfile.read('lab04/ex5/a_vowel.wav')

if len(signal.shape) > 1:
    signal = signal[:, 0]

n = len(signal)
group_size = int(0.01 * n) 
step_size = int(group_size * 0.5)

groups = []
for index in range(0, n-group_size + 1, step_size):
    group = signal[index:index+group_size]
    groups.append(group)

F = []
for group in groups:
    y = np.abs(np.fft.fft(group))
    F.append(y)

F = np.array(F).T

half_index = group_size // 2
F_half = F[:half_index, :]
F_db = 20 * np.log10(F_half + 1e-10)

max_time = len(signal) / fs
max_freq = fs / 2  # nyquist frequency in Hz

plt.figure(figsize=(12, 6))

plt.imshow(F_db, aspect='auto', origin='lower', extent=[0, max_time, 0, max_freq], cmap='inferno')

plt.title("Spectrogram")
plt.xlabel("Time (s)") 
plt.ylabel("Frequency (Hz)") 

colorbar = plt.colorbar()
colorbar.set_label('Magnitude (dB)')

plt.tight_layout()
plt.show()




