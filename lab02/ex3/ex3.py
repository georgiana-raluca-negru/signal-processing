import numpy as np
import scipy.io.wavfile
import sounddevice
import time

def sin_a(t):
    return np.sin(2*np.pi*400*t)

def sin_b(t):
    return np.sin(2*np.pi*800*t)

def sawtooth(t):
    return np.mod(t*240, 1)*2 - 1

def square(t):
    return np.sign(np.sin(2*np.pi*300*t))

fs = 44100
t = np.arange(0, 1, 1/fs) 

sig_a = sin_a(t)
sig_b = sin_b(t)
sig_c = sawtooth(t)
sig_d = square(t)

sounddevice.play(sig_a, samplerate=fs)
sounddevice.wait() 
time.sleep(0.5)    

sounddevice.play(sig_b, samplerate=fs)
sounddevice.wait()
time.sleep(0.5)

sounddevice.play(sig_c, samplerate=fs)
sounddevice.wait()
time.sleep(0.5)

sounddevice.play(sig_d, samplerate=fs)
sounddevice.wait()
time.sleep(0.5)

scipy.io.wavfile.write('lab02/ex3/saved_signal.wav', fs, sig_a)

rate, data = scipy.io.wavfile.read('lab02/ex3/saved_signal.wav')
sounddevice.play(data, samplerate=rate)
sounddevice.wait()