#Exercicio 1
#Aluno: Igor Gabriel Pereira
#Cod.: 825.399

!wget "https://github.com/igorgabriel12/Processamento-de-Sinais-e-Imagens/blob/master/Atividade2/pista_aeroporto.jpg?raw=true" -O "pista_aeroporto.jpg"
 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread('pista_aeroporto.jpg')
img2 = img1.copy()

img2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
img2 = cv.Canny(img2,500,200)
 
p1 = 100 
p2 = 80

linhas = cv.HoughLinesP(img2,1,np.pi/180, 120, minLineLength=p1, maxLineGap=p2)

if linhas is not None:
  print("________________________"  ) 
  print("\nLinhas encontradas: %i" %(len(linhas)))
  print("________________________"  ) 

  for linha in linhas:
    x1,y1,x2,y2 = linha[0]
    cv.line(img1, (x1,y1),(x2,y2), (255,0,0), 3)
else:
  print("________________________"  ) 
  print("\nNenhuma linha encontrada.")
  print("________________________"  ) 

plt.figure(figsize=(15,15))
plt.subplot(121), plt.imshow(img1) 