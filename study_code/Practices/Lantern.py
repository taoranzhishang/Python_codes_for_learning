# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
import wxgl.wxplot as plt

path = r"D:\code\py\study_code\Practices\Lantern\paper.png"
im = np.array(Image.open(path)) / 255
rows, cols, deep = im.shape

r, h = 1, 2 * np.pi * rows / cols
theta = np.linspace(0, 2 * np.pi, cols)
x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.linspace(0, h, rows)
xs = np.tile(x, (rows, 1))
ys = np.tile(y, (rows, 1))
zs = z.repeat(cols).reshape((rows, cols))

theta = np.linspace(0, 2 * np.pi, 18, endpoint=False)
x = r * np.cos(theta)
y = r * np.sin(theta)
x[2::3] = x[1::3]
x[1::3] = 0
y[2::3] = y[1::3]
y[1::3] = 0
z = np.ones(18) * h * 0.9
vs = np.stack((x, y, z), axis=1)

plt.mesh(xs, ys, zs, im[::-1])
plt.surface(vs, color='#C03000', method='T', mode='FCBC', alpha=0.8)
plt.sphere((0, 0, h * 0.4), 0.4, '#FFFFFF', slices=60, mode='FCBC')
plt.plot((0, 0), (0, 0), (0.4 * h, 1.5 * h), width=3.0, style="", cmap='hsv', caxis='z')
plt.show(rotation='h-')
