import cv2  # pip install opencv-python

img = cv2.imread('flower.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("Flower Photo", img)
cv2.waitKey(0) # causes a 'Secure Coding' warning on macOSX... not sure the exact cause but believe it i safe
cv2.destroyAllWindows()