from PIL import Image
import numpy as np

# This code assumes the image has only 3 channels: RGB.
# For transparent images with an alpha value, a minor modification is required
# Note that pixels start as 16-bit but we must convert back down to 8-bit

img_color = Image.open('flower.jpg')
pixels = np.array(img_color).astype(np.uint16)
print(pixels[0:2,0:2])

height, width, channels = pixels.shape

for y in range(height):
    for x in range(width):
        r, g, b = pixels[y][x]
        r = g = b = int((r + g + b) // 3)
        pixels[y][x] = [r, g, b]

img_gray = Image.fromarray(pixels.astype(np.uint8))
img_gray.show()