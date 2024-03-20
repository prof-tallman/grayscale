import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pixels = np.copy(mpimg.imread('flower.jpg'))
height, width, channels = pixels.shape

for y in range(height):
    for x in range(width):
        r, g, b = pixels[y][x]
        total = int(r) + int(g) + int(b)
        r = g = b = total // 3
        pixels[y][x] = [r, g, b]

plt.imshow(pixels)
plt.show()