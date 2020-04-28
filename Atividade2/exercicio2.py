#Exercicio 2
#Aluno: Igor Gabriel Pereira
#Cod.: 825.399

!wget "https://github.com/igorgabriel12/Processamento-de-Sinais-e-Imagens/blob/master/Atividade2/laranjas.jpg?raw=true" -O "laranjas.jpg"
 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('laranjas.jpg')
img2 = img1.copy()

img2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
img2 = cv.medianBlur(img2,5)

circulos = cv.HoughCircles(img2, cv.HOUGH_GRADIENT, 1,120, param1=120,param2=30,minRadius=0,maxRadius=0)
circulos = np.uint16(np.around(circulos))

if circulos is not None:
  print("__________________________________________________"  ) 
  print("\nForam detectadas %i laranjas inteiras nesta imagem." %(len(circulos[0,:])))
  print("__________________________________________________"  ) 

  for circulo in circulos[0,:]:
    cv.circle(img1,(circulo[0],circulo[1]),circulo[2],(0,255,0), 3)
    cv.circle(img2,(circulo[0],circulo[1]),circulo[2],(255,0,0), 3)

else:
    print("____________________________________________"  ) 
    print("\nNao foram detectadas laranjas nesta imagem.")
    print("____________________________________________"  ) 

img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)

plt.figure(figsize=(15,15))
plt.subplot(121), plt.imshow(img1)
plt.subplot(122), plt.imshow(img2, cmap='gray')