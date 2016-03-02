import cv2
import numpy as np

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape)/2)
  rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape,flags=cv2.INTER_LINEAR)
  return result

img = cv2.imread('IMG_5843.JPG',cv2.IMREAD_GRAYSCALE)
resized_image = rotateImage(img,270)
resized_image = cv2.resize(resized_image,(50,50))
cv2.imwrite('IMG_5843.JPG',resized_image)
cv2.imshow('IMG_5846.JPG',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
