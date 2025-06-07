# Animated Julia Set Fractal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Image dimensions
im_width, im_height = 400, 400

# Fractal parameters
nit_max = 200
zabs_max = 2
xmin, xmax = -1.5, 1.5
ymin, ymax = -1.5, 1.5

# Animation parameters
frames = 60
radius = 0.7885


def julia_set(c):
    julia = np.zeros((im_height, im_width))
    for ix, x in enumerate(np.linspace(xmin, xmax, im_width)):
        for iy, y in enumerate(np.linspace(ymin, ymax, im_height)):
            z = complex(x, y)
            nit = 0
            while abs(z) <= zabs_max and nit < nit_max:
                z = z**2 + c
                nit += 1
            julia[iy, ix] = nit
    return julia


print("Generating animation frames...")
fig, ax = plt.subplots()
im = ax.imshow(np.zeros((im_height, im_width)), cmap="twilight", animated=True)
ax.axis("off")


def update(frame):
    angle = 2 * np.pi * frame / frames
    c = radius * complex(np.cos(angle), np.sin(angle))
    data = julia_set(c)
    im.set_array(data)
    ax.set_title(f"c = {c.real:+.3f}{c.imag:+.3f}i")
    return [im]


ani = FuncAnimation(fig, update, frames=frames, interval=100, blit=True)
ani.save("julia_animation.gif", writer=PillowWriter(fps=15))
plt.show()
