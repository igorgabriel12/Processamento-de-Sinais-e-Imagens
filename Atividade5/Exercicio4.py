# Aluno: Igor Gabriel Pereira
# Cod.: 825.399
# Exercicio 4

## OBS: Solução incompleta

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

path = '/content/drive/My Drive/Disciplinas/Processamento de Sinais e Imagens/image_dataset_publico/'
path_dataset = path + "face_dataset/"
 

lista_faces = []
lista_classes = []
 
for diretorio in os.listdir(path_dataset):
  classe = int(diretorio.replace("p",""))
  print("Classe: %i " %(classe) )

 
  for imagem in os.listdir(path_dataset + diretorio):
    print("   - %s " %(imagem))

  
    face = cv.imread(path_dataset+diretorio+"/"+imagem)
    face = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
 
    lista_faces.append(face)
    lista_classes.append(classe)

 
modelo = cv.face.EigenFaceRecognizer_create()
modelo.train(lista_faces, np.array(lista_classes))
 
img_teste = cv.imread(path_dataset + "p1/6.jpg")
img_teste = cv.cvtColor(img_teste, cv.COLOR_BGR2GRAY)

resultado = modelo.predict(img_teste)
print(resultado)

img_teste = cv.imread(path + "rosto_3.jpg")
img_teste = cv.cvtColor(img_teste, cv.COLOR_BGR2GRAY)

resultado = modelo.predict(img_teste)
print(resultado)