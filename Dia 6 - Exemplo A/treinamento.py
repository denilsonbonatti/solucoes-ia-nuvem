#pip uninstall opencv-python
#pip install opencv-contrib-python

import cv2
import os
import numpy as np

pasta_base = 'fotos_base'
faces = []
ids = []
label_map = {}
label_id = 0

print("[INFO] Iniciando treinamento...")

for nome_arquivo in os.listdir(pasta_base):
    caminho = os.path.join(pasta_base, nome_arquivo)
    imagem = cv2.imread(caminho)

    if imagem is None:
        print(f"[ERRO] Não foi possível carregar a imagem: {caminho}")
        continue

    # Converte para tons de cinza
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Nome da pessoa = nome do arquivo sem extensão
    nome = os.path.splitext(nome_arquivo)[0]

    # Atribui um ID numérico
    if nome not in label_map:
        label_map[nome] = label_id
        label_id += 1

    faces.append(imagem_gray)
    ids.append(label_map[nome])
    print(f"[INFO] Adicionada imagem para {nome}")

# Treinamento
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(ids))
recognizer.save("modelo.yml")

# Salvar o mapa de nomes para ID
import pickle
with open("labels.pkl", "wb") as f:
    pickle.dump(label_map, f)

print("[INFO] Treinamento concluído com sucesso!")
