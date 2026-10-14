import matplotlib.pyplot as plt
import numpy as np

# 2pi*400t + 0
# frequency of signal 400 (400 full circles in a second)
def sin_a(t):
    return np.sin(2*np.pi*400*t)

# 2pi*800t + 0
# frequency of signal 800 (800 full circles in a second)
def sin_b(t):
    return np.sin(2*np.pi*800*t)

# 240 teeht per second
def sawtooth(t):
    return np.mod(t*240, 1)

# overlapping with the sine singnal
def square(t):
    return np.sign(np.sin(2*np.pi*300*t))

# a)
# 1600 = 4*400
no_samples_a = 1600
l_inf_a = 0
l_sup_a = 0.25

r_a = np.linspace(start=l_inf_a, stop=l_sup_a, num=no_samples_a)

# first 50 samples
plt.plot(r_a[:50], sin_a(r_a[:50]))
plt.stem(r_a[:50], sin_a(r_a[:50]))
plt.title("a) 400 Hz Sin (primele 50 esantioane)")
plt.savefig("lab01/2.a.pdf")
plt.show()

# b)
# 800 full circles per second, so at least 800*4 points per second
no_samples_b = 800*4*3
l_inf_b = 0
l_sup_b = 3

r_b = np.linspace(start=l_inf_b, stop=l_sup_b, num=no_samples_b)

plt.plot(r_b[:50], sin_b(r_b[:50]))
plt.stem(r_b[:50], sin_b(r_b[:50]))
plt.title("b) 800 Hz Sin (primele 50 esantioane)")
plt.savefig("lab01/2.b.pdf")
plt.show()

# c)
# 240 teeth per second, sample a decent amount of points for each tooth
no_samples_c = 240*20
l_inf_c = 0
l_sup_c = 1
r_c = np.linspace(start=l_inf_c, stop=l_sup_c, num=no_samples_c)

plt.plot(r_c[:60], sawtooth(r_c[:60]))
plt.stem(r_c[:60], sawtooth(r_c[:60]))
plt.title("c) 240 Hz sawtooth (primele 60 esantioane)")
plt.savefig("lab01/2.c.pdf")
plt.show()

# d)
no_samples_d = 300*20
l_inf_d = 0
l_sup_d = 1
r_d = np.linspace(start=l_inf_d, stop = l_sup_d, num=no_samples_d)

plt.plot(r_d[:60], square(r_d[:60]))
plt.stem(r_d[:60], square(r_d[:60]))
plt.title("d) 300 Hz square (primele 60 esantioane)")
plt.savefig("lab01/2.d.pdf")
plt.show()

# e)
# rows and columns
n = 128
m = 128

# return numpy array of dimension n*m, all elements randomized
I = np.random.rand(n, m)
plt.imshow(I, cmap='gray')
plt.title("e) Semnal 2D aleator")
plt.savefig("lab01/random_signal.pdf")
plt.show()

# f)
I = np.ones((n, m))
plt.imshow(I, cmap='gray')
plt.title("e) Semnal 2D aleator")
plt.savefig("lab01/custom_signal.pdf")
plt.show()



