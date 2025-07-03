#pip install SpeechRecognition

import speech_recognition as sr

# Inicializa o reconhecedor
recognizer = sr.Recognizer()

# Carrega o áudio de um arquivo WAV
with sr.AudioFile(r"arquivo.wav") as source:
    audio = recognizer.record(source)

# Transcreve o áudio usando a API do Google (gratuita, limitada)
try:
    texto = recognizer.recognize_google(audio, language="pt-BR")
    print("Texto transcrito:", texto)
except sr.UnknownValueError:
    print("Não foi possível entender o áudio.")
except sr.RequestError as e:
    print(f"Erro ao requisitar serviço: {e}")
