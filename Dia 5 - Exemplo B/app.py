from tkinter import *
from tkinter.scrolledtext import ScrolledText
from openai import AzureOpenAI

# Configurações do Azure OpenAI
endpoint = "???"
deployment = "gpt-4.1"
subscription_key = "??"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# Função para enviar a pergunta e exibir a resposta
def enviar_mensagem():
    pergunta = entrada.get()
    if not pergunta.strip():
        return
    chatbox.insert(END, "Você: " + pergunta + "\n")
    entrada.delete(0, END)

    try:
        resposta = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": pergunta}
            ],
            max_completion_tokens=800,
            temperature=1.0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        texto = resposta.choices[0].message.content
        chatbox.insert(END, "Assistente: " + texto + "\n\n")
    except Exception as e:
        chatbox.insert(END, "Erro: " + str(e) + "\n\n")

# Interface gráfica com Tkinter
janela = Tk()
janela.title("Chatbot com Azure OpenAI")
janela.geometry("600x400")

chatbox = ScrolledText(janela, wrap=WORD, state='normal')
chatbox.pack(padx=10, pady=10, fill=BOTH, expand=True)

entrada = Entry(janela, width=80)
entrada.pack(padx=10, pady=(0,10), side=LEFT, fill=X, expand=True)

botao_enviar = Button(janela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack(padx=(0,10), pady=(0,10), side=RIGHT)

janela.mainloop()
