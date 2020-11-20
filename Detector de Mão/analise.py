import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier("treinamento/resultado.xml")

image = cv2.imread("teste01.jpg")
height, width, c = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
objetos = car_cascade.detectMultiScale(gray, 1.2, 5)
print(objetos)
for (x,y,w,h) in objetos:
    cv2.rectangle(image,(x,y), (x+w,y+h),(0,0,255),2)
cv2.imshow('Analise', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
