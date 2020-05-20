# Aluno: Igor Gabriel Pereira
# Cod.: 825.399
# Exercicio 3

## OBS: Gostaria de ter tirado uma duvida a respeto deste exercicio sobre como reproduir o video normal, sem que fosse apenas os frames

!wget "https://vimeo.com/277147027" -O "teste.MP4"
 
import cv2
from google.colab.patches import cv2_imshow
path = '/content/drive/My Drive/Disciplinas/Processamento de Sinais e Imagens/image_dataset_publico/'
 
face_cascade = cv2.CascadeClassifier(path + "cascades/haarcascade_frontalface_default.xml")
 
cap = cv2.VideoCapture('video.mp4')

while True: 
    _, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) 
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2_imshow(img)
     
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
 
cap.release()