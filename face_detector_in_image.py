import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('3333.jpg')

grayscald_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(grayscald_img)

#print(face_coordinates)

for (x,y,w,h) in face_coordinates: 
     cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(255),randrange(255),randrange(255)),2)


cv2.imshow('Image Detector', img)



cv2.waitKey()