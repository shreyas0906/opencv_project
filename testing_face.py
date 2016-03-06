import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
sunglasses_cascade = cv2.CascadeClassifier('cascade_sunglasses.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img  = cv2.resize(img,(640,480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,150,150),1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.imshow('Region_color',roi_color)
        cv2.imhsow('Region_gray',roi_gray)
         for (ex,ey,ew,eh) in faces:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(190,160,110),1)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()