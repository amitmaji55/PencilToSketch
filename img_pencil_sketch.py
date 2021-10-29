import cv2

image = cv2.imread('test.jpg')

grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert_img = cv2.bitwise_not(grey_img)

blur_img = cv2.GaussianBlur(invert_img, (31,21), 00)

inverted_img = cv2.bitwise_not(blur_img)

sketch = cv2.divide(grey_img, inverted_img, scale=256.0)

cv2.imwrite('sketch.png', sketch)