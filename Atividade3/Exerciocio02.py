#Exercicio 2
#Aluno: Igor Gabriel Pereira
#Cod.: 825.399

!wget "https://avatars0.githubusercontent.com/u/15963786?s=460&u=c0be7b89d0cccdbc0aec6c2acb5357c8ad7d1496&v=4" -O "eu.jpg"

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('eu.jpg')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
 
img2 = img1.copy()
p1 = (60,0) 
p2 = (260,300)  
img2 = cv.rectangle(img2,p1,p2,(255,0,0),2)

mascara = np.zeros(img1.shape[:2], np.uint8)
bgModel = np.zeros((1,65), np.float64)
fgModel = np.zeros((1,65), np.float64)
retangulo = p1+p2

cv.grabCut(img1, mascara, retangulo, bgModel, fgModel, 5, cv.GC_INIT_WITH_RECT)

filtro = np.where ( (mascara == 0) | (mascara == 2),0,1).astype('uint8')
img3 = img1.copy()
img3 = img3*filtro[:,:,np.newaxis]

plt.figure(figsize=(20,20))
plt.subplot(131), plt.imshow(img1)
plt.subplot(132), plt.imshow(img2)
plt.subplot(133), plt.imshow(img3)