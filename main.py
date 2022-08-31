# virtualenv julia-set
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Constants affecting fractal output
im_width, im_height = 1500, 1500
nit_max = 150
c = complex(-1.1, 0.185)
zabs_max = 150
xmin, xmax = -1.9, 1.9
xwidth = xmax - xmin
ymin, ymax = -1.2, 1.2
yheight = ymax - ymin

# julia = np.zeros()
# julia = np.zeros((im_height, im_width), dtype=np.dtype())
def make_row():
	return np.zeros((im_width, 3))
julia = np.array([make_row() for i in range(0, im_height)])

print('\n -- Beginning iteration... \n')
print('z = z^2 + c')
print('c = %si + %sj\n' % (c.imag, c.real))

for ix in range(im_width):
	for iy in range(im_height):
		nit = 0
		z = complex(
			ix / im_width * xwidth + xmin,
			iy / im_height * yheight + ymin,
		)
		while abs(z) <= zabs_max and nit < nit_max:
			z = z**2 + c
			nit += 1

		shade = nit / nit_max
		zshade = (z / zabs_max).imag

		julia[iy][ix] = np.array([zshade*1, zshade*10, zshade*10])

print('making image & plot...')
fig, ax = plt.subplots()
ax.imshow(julia, interpolation='none')

# labels
xtick_labels = np.linspace(xmin, xmax, int(xwidth / 0.5))
ax.set_xticks([(x-xmin) / xwidth * im_width for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
ytick_labels = np.linspace(ymin, ymax, int(yheight / 0.5))
ax.set_yticks([(y-ymin) / yheight * im_height for y in ytick_labels])
ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])

print('writing fractal...')
plt.savefig('Green_jello_salad_%s_%si_%sj.png' % (
	random.randint(0,10000), c.imag, c.real,
))
plt.show()
