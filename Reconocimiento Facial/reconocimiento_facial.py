import cv2

def faciales(detected,image,color: tuple):
    for (x,y,width,height) in detected:
        cv2.rectangle(
            image,
            (x,y),
            (x+width, y + height),
            color,
            thickness=2
        )
        
cap = cv2.VideoCapture(0)
cara =cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
ojo = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")


while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    caras = cara.detectMultiScale( image=gray,scaleFactor=1.3, minNeighbors=4)
    ojos = ojo.detectMultiScale(image=gray, scaleFactor=1.3, minNeighbors=4)
    "caras = cara.detectMultiScale(gray,1.1,4)"
    faciales(caras, img, (0, 0, 255))
    faciales(ojos, img, (0, 255, 0))
    
    cv2.imshow('Deteccion de Rostro',img)
    
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()