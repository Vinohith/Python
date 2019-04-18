import numpy as np
import cv2

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
	# initialize the dimensions of the image to be resized and grab the image size
	dim = None
	(h, w) = image.shape[:2]
	# if both the width and height are None, then return the original image
	if width is None and height is None:
		return image
		# check to see if the width is None
	if width is None:
		# calculate the ratio of the height and construct the dimensions
		r = height / float(h)
		dim = (int(w * r), height)
	# otherwise, the height is None
	else:
		# calculate the ratio of the width and construct the dimensions
		r = width / float(w)
		dim = (width, int(h * r))
	# resize the image
	resized = cv2.resize(image, dim, interpolation = inter)
	# return the resized image
	return resized

def order_points(pts):
	rect = np.zeros((4, 2), dtype = "float32")

	sum_of_pts = np.sum(pts, axis = 1) 
	rect[0] = pts[np.argmin(sum_of_pts)]
	rect[2] = pts[np.argmax(sum_of_pts)]

	diff_of_pts = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff_of_pts)]
	rect[3] = pts[np.argmax(diff_of_pts)]

	return rect

def four_point_transform(image, pts):
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	# (tr, tl, bl, br) = rect

	height_left = np.linalg.norm(tl - bl)
	height_right = np.linalg.norm(tr - br)
	height = np.maximum(int(height_left), int(height_right))

	width_top = np.linalg.norm(tl - tr)
	width_bottom = np.linalg.norm(bl - br)
	width = np.maximum(int(width_top), int(width_bottom))

	new_rect = np.array([[0, 0], [width, 0], [width, height], [height, 0]], dtype = "float32")

	M = cv2.getPerspectiveTransform(rect, new_rect)
	result = cv2.warpPerspective(image, M, (width, height))

	return result

