import cv2
import numpy as np

img = cv2.imread("image4.png")

white_lower = np.asarray([230, 230, 230])
white_upper = np.asarray([255, 255, 255])

mask = cv2.inRange(img, white_lower, white_upper)
mask = cv2.bitwise_not(mask)



cnt, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
largest_contour = max(cnt, key=lambda x:cv2.contourArea(x))
bounding_rect = cv2.boundingRect(largest_contour)

cropped_image = img[bounding_rect[1]: bounding_rect[1]+bounding_rect[3],
                bounding_rect[0]:bounding_rect[0]+bounding_rect[2]]


cv2.imwrite("image4new.png", cropped_image)