import numpy as np 
import cv2
from transform import four_point_transform, resize

# image = cv2.imread(args['image'])
image = cv2.imread('receipt-outlined.jpg')
ratio = image.shape[0] / 500.0
orginal_image = np.copy(image)
image = resize(image, height = 500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edged = cv2.Canny(blur, 60, 200)

cnts = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[1]
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
# print(cnts)

for c in cnts:
	perimeter = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
	if len(approx) == 4:
		cnt = approx
		break

cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)


warped = four_point_transform(orginal_image, cnt.reshape(4, 2)*ratio)
# warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
# T = threshold_local(warped, 11, offset = 10, method = "gaussian")
# warped = (warped > T).astype("uint8") * 255

cv2.imshow('result', resize(warped, height = 650))
cv2.imshow('original image', resize(orginal_image, height = 650))


cv2.waitKey(0)
cv2.destroyAllWindows()