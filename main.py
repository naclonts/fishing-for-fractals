# virtualenv julia-set
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

im_width, im_height = 2000, 1250
nit_max = 2000
c = complex(-0.9, 0.265)
zabs_max = 10
xmin, xmax = -1.7, 1.7
xwidth = xmax - xmin
ymin, ymax = -1, 1
yheight = ymax - ymin

# julia = np.zeros()
# julia = np.zeros((im_height, im_width), dtype=np.dtype())
def make_row():
	return np.zeros((im_width, 3))
julia = np.array([make_row() for i in range(0, im_height)])

print('beginning iteration...')
print('z = z^2 + c')
print('c = %si + %sj' % (c.imag, c.real))
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
		# shade = 1 - nit / nit_max
		shade = (nit / nit_max) * 255
		julia[iy][ix] = np.array([shade/4, shade/2, shade*1.0])
		# if diff < 200 and diff > 1:
		# 	julia[ix, iy] = 1
		# else:
		# 	julia[ix, iy] = 1 - diff / nit_max

print('making image & plot...')
fig, ax = plt.subplots()
ax.imshow(julia, interpolation='none')

# labels
xtick_labels = np.linspace(xmin, xmax, xwidth / 0.5)
ax.set_xticks([(x-xmin) / xwidth * im_width for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
ytick_labels = np.linspace(ymin, ymax, yheight / 0.5)
ax.set_yticks([(y-ymin) / yheight * im_height for y in ytick_labels])
ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])

print('writing fractal...')
plt.savefig('D:\\media\\fractals\\exploring julia set\\Fishing_for_fractals_%s' % random.randint(0,1000))
plt.show()
