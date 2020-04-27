# Exercicio 02
# Aluno: Igor Gabriel Pereira     
#Cod.: 825.399
 
!wget "https://github.com/igorgabriel12/Processamento-de-Sinais-e-Imagens/blob/master/Atividade1/moedas.jpg?raw=true" -O "moedas.jpg"

import math 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img1 = cv.imread("moedas.jpg")
img2 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
img3 = cv.cvtColor(img2,cv.COLOR_RGB2GRAY)

img4 = img3
all_radius = []
  
for lin in range(img3.shape[0]):
  for col in range(img3.shape[1]):
    if(img3.item(lin, col) > 50):
      img4.itemset((lin, col),0)
    else: 
      img4.itemset((lin, col),255)
    
contours, ordem = cv.findContours(img4, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
 
for c in contours:
  x, y, w, h = cv.boundingRect(c)
  cv.rectangle(img4, (x,y), (x+w, y+h), (255, 0, 0), 2) 
  area = cv.minAreaRect(c)
  
  box = cv.boxPoints(area) 
  box = np.int0(box) 

  (x, y), radius = cv.minEnclosingCircle(c)  
  all_radius.append(radius)
  
one_real_coin = round(math.pi * (all_radius[4] * all_radius[4]), 2)
five_cents_coin = round(math.pi * (all_radius[5] * all_radius[5]), 2)


print("_________________________________________________") 
print("\nMoeda de 1 real, área:", {one_real_coin}) 
print("Moeda de 5 centavos, área:", {five_cents_coin})
print("_________________________________________________")

# img4 = cv.cvtColor(img4,cv.COLOR_GRAY2RGB)
# img4 = cv.cvtColor(img4,cv.COLOR_RGB2BGR)

plt.figure(figsize=(8,8)) 
plt.subplot(111), plt.imshow(img4, cmap='binary')
# plt.subplot(332), plt.imshow(img2, cmap='binary') 