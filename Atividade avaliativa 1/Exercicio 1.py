# Exercício 01
# Aluno: Igor Gabriel Pereira     
#Cod.: 825.399

# Buscar imagem no Github

import cv2 as cv 
import matplotlib.pyplot as plt

img1 = cv.imread("objects.png");
img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)

img2 = cv.cvtColor(img1,cv.COLOR_RGB2GRAY)
 
ret, img2 = cv.threshold(img2,127,255,cv.THRESH_BINARY)
 
contorno, ordem = cv.findContours(img2, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

for c in contorno: 
  x,y,w,h = cv.boundingRect(c)
  cv.rectangle(img1,(x,y),(x+w,y+h),(255,242,0),2)
 
plt.figure(figsize=(8,8))
plt.imshow(img1)