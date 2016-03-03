import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
sunglasses_cascade = cv2.CascadeClassifier('cascade_sunglasses.xml')
#eye_cascade  cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img  = cv2.resize(img,(640,480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # find the sungalasses within the face



    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print "w", w, "h", h , "x", x , "y", y
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        area = img[y:y+h+15,x:x+w+15]

        #eyes = eye_cascade.detectMultiScale(roi_gray)
        sunglasses = sunglasses_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in sunglasses:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('area',area)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()