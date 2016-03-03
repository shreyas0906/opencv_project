import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
sunglasses_cascade = cv2.CascadeClassifier('cascade_sunglasses.xml')

img = cv2.imread('IMG_5843.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image',img)
#sunglasses = sunglasses_cascade.detectMultiscale(img)
# cv2.imshow('resized',resized)
for (x,y,w,h) in sunglasses:
         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)

cv2.waitKey(0)
cv2.destroyAllWindows()

