import cv2
import pickle

# Carregar modelo e labels
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("modelo.yml")

with open("labels.pkl", "rb") as f:
    label_map = pickle.load(f)
    id_to_nome = {v: k for k, v in label_map.items()}

# Detector de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Iniciar webcam
video = cv2.VideoCapture(0)
print("[INFO] Pressione 'q' ou 'ESC' para sair.")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in rostos:
        roi_gray = gray[y:y+h, x:x+w]
        id_pred, confianca = recognizer.predict(roi_gray)

        if confianca < 100:
            nome = id_to_nome.get(id_pred, "Desconhecido")
            texto = f"{nome} ({int(confianca)})"
        else:
            texto = "Desconhecido"

        print(f"[DEBUG] {texto}")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Reconhecimento Facial", frame)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == ord('q') or tecla == 27:  # Tecla 'q' ou ESC (27)
        break

video.release()
cv2.destroyAllWindows()
