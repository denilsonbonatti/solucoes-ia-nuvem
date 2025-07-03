import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr

def selecionar_arquivo():
    caminho = filedialog.askopenfilename(
        title="Selecione um arquivo de áudio WAV",
        filetypes=[("Arquivos WAV", "*.wav")]
    )
    if caminho:
        transcrever_audio(caminho)

def transcrever_audio(caminho_audio):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(caminho_audio) as source:
            texto_status.set("Reconhecendo...")
            janela.update()
            audio = recognizer.record(source)

        texto = recognizer.recognize_google(audio, language="pt-BR")
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(tk.END, texto)
        texto_status.set("Transcrição concluída.")
    except sr.UnknownValueError:
        messagebox.showerror("Erro", "Não foi possível entender o áudio.")
        texto_status.set("Falha no reconhecimento.")
    except sr.RequestError as e:
        messagebox.showerror("Erro", f"Erro ao acessar o serviço: {e}")
        texto_status.set("Erro de conexão.")

# Interface gráfica
janela = tk.Tk()
janela.title("Transcrição de Áudio (SpeechRecognition)")
janela.geometry("520x320")

botao_selecionar = tk.Button(janela, text="Selecionar Arquivo de Áudio", command=selecionar_arquivo)
botao_selecionar.pack(pady=10)

# Frame para texto + scrollbar
frame_texto = tk.Frame(janela)
frame_texto.pack(pady=10, expand=True, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame_texto)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

resultado_texto = tk.Text(frame_texto, wrap=tk.WORD, height=10, width=60, yscrollcommand=scrollbar.set)
resultado_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=resultado_texto.yview)

texto_status = tk.StringVar()
texto_status.set("Aguardando seleção de áudio...")
status_label = tk.Label(janela, textvariable=texto_status)
status_label.pack()

janela.mainloop()
