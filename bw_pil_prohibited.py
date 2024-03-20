from PIL import Image

img_color = Image.open('flower.jpg')
img_gray = img_color.convert('LA')
img_color.show()
img_gray.show()