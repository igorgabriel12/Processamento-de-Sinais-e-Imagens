# Aluno: Igor Gabriel Pereira
# cod.: 825.399
# Exercicio 1

!wget "https://github.com/igorgabriel12/Processamento-de-Sinais-e-Imagens/blob/master/Atividade4/celulas.jpg?raw=true"  -O "celulas.png"

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('celulas.png')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)

img2 = cv.cvtColor(img1, cv.COLOR_RGB2GRAY)
ret, img2 = cv.threshold(img2,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
img3 = cv.morphologyEx(img2, cv.MORPH_OPEN, kernel, iterations = 2)
img4 = cv.dilate(img3,kernel,iterations=3)

img5 = cv.distanceTransform(img3, cv.DIST_L2, 5)
ret,img6 = cv.threshold(img5,0.70*img5.max(), 255, 0)

img6 = np.uint8(img6)
img7 = cv.subtract(img4, img6)

ret, rotulos = cv.connectedComponents(img6)
rotulos = rotulos + 1

rotulos[img7 == 255] = 0
img8 = cv.watershed(img1,rotulos)
img1[rotulos == -1] = [255,0,0]

plt.figure(figsize=(15,10))
plt.subplot(241), plt.imshow(img1), plt.axis("off")
plt.subplot(242), plt.imshow(img2,cmap='binary'), plt.title("binária"), plt.axis("off")
plt.subplot(243), plt.imshow(img3,cmap='binary'), plt.title("abertura"), plt.axis("off")
plt.subplot(244), plt.imshow(img4,cmap='binary'), plt.title("dilatação"), plt.axis("off")
plt.subplot(245), plt.imshow(img5,cmap='gray'), plt.title("trans.distância"), plt.axis("off")
plt.subplot(246), plt.imshow(img6,cmap='binary'), plt.title("trans.distância+threshold"), plt.axis("off")
plt.subplot(247), plt.imshow(img7,cmap='binary'), plt.title("subtração"), plt.axis("off")
plt.subplot(248), plt.imshow(img8,cmap='jet'), plt.title("resultado"), plt.axis("off")
plt.show()