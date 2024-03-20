import image

img_color = image.FileImage('flower.jpg')
w = img_color.getWidth()
h = img_color.getHeight()

img_gray = image.EmptyImage(w, h)
for y in range(h):
    for x in range(w):
        pixel = img_color.getPixel(x, y)
        totIntensity = pixel.getRed() + pixel.getGreen() + pixel.getBlue()
        avgIntensity = totIntensity // 3
        bstIntensity = min(avgIntensity, 255)
        pixel = image.Pixel(bstIntensity, bstIntensity, bstIntensity)
        img_gray.setPixel(x, y, pixel)

window = image.ImageWin(w, h, "Grayscale Image")
img_gray.draw(window)
window.exitonclick()