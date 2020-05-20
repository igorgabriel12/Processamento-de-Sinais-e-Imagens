# Aluno: Igor Gabriel Pereira
# Cod.: 825.399
# Exercicio 2

!wget "https://avatars0.githubusercontent.com/u/15963786?s=460&u=c0be7b89d0cccdbc0aec6c2acb5357c8ad7d1496&v=4" -O "eu.jpg" 

img1 = cv.imread("eu.jpg" )
img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier("/content/drive/My Drive/Disciplinas/Processamento de Sinais e Imagens/image_dataset_publico/cascades/haarcascade_eye.xml")

res = face_cascade.detectMultiScale(img2, scaleFactor = 1.2, minNeighbors = 7)

if res is not None:
  print("Olhos detectados: %i" %(len(res)))
 
  for (x,y,larg,alt) in res:
    img1 = cv.rectangle(img1, (x,y),(x+larg,y+alt), (0,128,0), 2)

else:
  print("Nenhum olho detectado.")


plt.figure(figsize=(10,10))
plt.imshow(img1), plt.axis("off")
plt.show()