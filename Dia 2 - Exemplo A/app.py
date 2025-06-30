import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import requests

# === CONFIGURAÇÕES DO AZURE ===
subscription_key = "????"
endpoint = "??????"  
analyze_url = endpoint + "vision/v3.2/analyze"

params = {
    "visualFeatures": "Description,Objects",
    "language": "pt"
}

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/octet-stream"
}

# === FUNÇÃO PRINCIPAL ===
def analisar_imagem():
    caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg;*.png")])
    if not caminho:
        return

    # Abre e mostra imagem
    imagem = Image.open(caminho)
    imagem.thumbnail((400, 400))
    img_tk = ImageTk.PhotoImage(imagem)
    painel.config(image=img_tk)
    painel.image = img_tk

    # Lê binário da imagem
    with open(caminho, "rb") as f:
        img_data = f.read()

    try:
        response = requests.post(analyze_url, headers=headers, params=params, data=img_data)
        response.raise_for_status()
        resultado = response.json()

        descricao = resultado["description"]["captions"][0]["text"]
        objetos = resultado.get("objects", [])

        texto_resultado = f"📝 Descrição: {descricao}\n\n🎯 Objetos detectados:\n"
        for obj in objetos:
            texto_resultado += f" - {obj['object']} (confiança: {obj['confidence']:.2f})\n"

        txt_resultado.config(state="normal")
        txt_resultado.delete("1.0", tk.END)
        txt_resultado.insert(tk.END, texto_resultado)
        txt_resultado.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Erro", str(e))

# === INTERFACE GRÁFICA ===
janela = tk.Tk()
janela.title("Análise de Imagem - Azure Computer Vision")
janela.geometry("600x700")

btn_abrir = tk.Button(janela, text="Selecionar Imagem", command=analisar_imagem)
btn_abrir.pack(pady=10)

painel = tk.Label(janela)
painel.pack()

txt_resultado = tk.Text(janela, height=15, width=70, state="disabled")
txt_resultado.pack(pady=10)

janela.mainloop()
