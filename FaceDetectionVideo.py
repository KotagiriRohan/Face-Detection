import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    _,image = cap.read()
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow('face',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()