#pip install azure-cognitiveservices-speech

import azure.cognitiveservices.speech as speechsdk

# Substitua com suas credenciais
speech_key = ""
service_region = "eastus" 

# Configuração
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Arquivo de áudio (formato WAV recomendado)
audio_input = speechsdk.AudioConfig(filename=r"C:\Users\denilson.lbonatti\Documents\solucoes-ia-nuvem\Dia 4 - Exemplo A\exemplo2.wav")

# Criação do reconhecedor
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

# Transcrição
print("Transcrevendo...")
result = speech_recognizer.recognize_once()

# Resultado
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Texto:", result.text)
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("Não reconhecido.")
else:
    print("Erro:", result.reason)
