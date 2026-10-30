import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

def sine(t):
    return np.sin(2*np.pi*t*6)

l_inf = 0
l_sup = 1
fs = 1000
r = np.arange(l_inf, stop=l_sup, step=1/fs)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

ax1.plot(r, sine(r), color = "pink")
ax1.set_title("Sine signal of frequency 6Hz")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")

# wrapping frequency is of 1, from the formula
# it determines the speed used to wrap the fignal 
# one wrap of the unit circle per second
y = sine(r)*math.e**(-2*np.pi*1j*r*1)

ax2.plot(np.real(y), np.imag(y), color= "purple")
ax2.set_title("Wrapped Sine signal")
ax2.set_xlabel("Real")
ax2.set_ylabel("Imaginary")
ax2.set_aspect('equal')

plt.tight_layout()
plt.savefig("lab03/ex2/figura_1.pdf")
plt.show()

# ===================================================================================================================

# different values for omega
omega = [2, 3, 6, 8]
fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (12,10), layout='constrained')

# all distances and components calculated before
y_wrapped_all = [sine(r) * np.exp(-2*np.pi*1j*r*o) for o in omega]
distances_all = [np.abs(y_w) for y_w in y_wrapped_all]

scatters = []
indicators = []

# using zip so i can go with both omega and the axis in parallel
for ax, o in zip(axs.flat, omega):
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_title(f"Wrapping frequency omega {o} Hz")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.set_aspect('equal')

    # origin of each subplot
    ax.plot(0, 0, 'ko', markersize=6, label="Origin") 
    # horizontal axis
    ax.axhline(0, color='grey', linestyle='-', linewidth=0.8) 
    # vertical axis
    ax.axvline(0, color='grey', linestyle='-', linewidth=0.8) 

    sc = ax.scatter([], [], c=[], cmap='viridis', vmin=0, vmax=1, s=8)

    # the moving indicator pointing to the active sample point in animation
    ind, = ax.plot([], [], 'ro', markersize=6, zorder=6)
    fig.colorbar(sc, ax=ax, label="Distance from Origin", shrink=0.8)

    scatters.append(sc)
    indicators.append(ind)

def update_fig(frame):
    artists = []
    for i in range(len(omega)):
        # slicing the arrays up until index (we have eveything from before and one more on each frame)
        y_slice = y_wrapped_all[i][:frame]
        d_slice = distances_all[i][:frame]

        # at first we have nothig to sample
        if len(y_slice) > 0:
            # the coordinates 
            pts = np.column_stack((np.real(y_slice), np.imag(y_slice)))
            scatters[i].set_offsets(pts)
            scatters[i].set_array(d_slice)
            
            # position red dot marker at current leading point
            curr_y = y_wrapped_all[i][frame-1]
            indicators[i].set_data([np.real(curr_y)], [np.imag(curr_y)])

        artists.extend([scatters[i], indicators[i]])
    return artists

# rendering all te points for the final pdf save
update_fig(len(r))
plt.savefig("lab03/ex2/different_wrapping_frequencies.pdf")

# 2resetting the indicators and scatter plot for the animation
for sc in scatters:
    sc.set_offsets(np.empty((0, 2)))
    sc.set_array(np.empty((0,)))

for ind in indicators:
    ind.set_data([], [])

# starting the animation with 4 points/steps per second
frame_sequence = list(range(1, len(r) + 1, 4))
ani2 = FuncAnimation(fig, update_fig, frames=frame_sequence, interval=1, repeat=False)

plt.show()
