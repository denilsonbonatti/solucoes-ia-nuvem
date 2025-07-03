# pip install azure-ai-textanalytics
#recurso: "Azure AI Language"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Substitua pelos seus dados
endpoint = ""
key = ""

# Autenticação
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Comentários de exemplo
comentarios = [
    "Esse produto é maravilhoso, superou minhas expectativas!",
    "Horrível, chegou quebrado e o suporte não ajudou.",
    "É ok, nada demais, mas cumpre o que promete."
]

# Análise de sentimentos
response = client.analyze_sentiment(documents=comentarios)

# Exibir resultados
for idx, doc in enumerate(response):
    print(f"Comentário: {comentarios[idx]}")
    print(f"Sentimento: {doc.sentiment}")
    print(f"Confiança: Positivo={doc.confidence_scores.positive:.2f}, "
          f"Neutro={doc.confidence_scores.neutral:.2f}, "
          f"Negativo={doc.confidence_scores.negative:.2f}")
    print("-" * 50)
