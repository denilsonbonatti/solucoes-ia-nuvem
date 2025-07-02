import pandas as pd
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError

# Substitua pelos seus dados reais
AZURE_ENDPOINT = "????"
AZURE_KEY = "????"

# Autenticação
def authenticate_client(endpoint, key):
    credential = AzureKeyCredential(key)
    return TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Análise de sentimentos
def analisar_sentimentos(client, comentarios):
    response = client.analyze_sentiment(documents=comentarios)
    resultados = []
    for idx, doc in enumerate(response):
        if not doc.is_error:
            resultados.append({
                "comentario": comentarios[idx],
                "sentimento": doc.sentiment,
                "positivo": doc.confidence_scores.positive,
                "neutro": doc.confidence_scores.neutral,
                "negativo": doc.confidence_scores.negative
            })
        else:
            resultados.append({
                "comentario": comentarios[idx],
                "erro": doc.error.message
            })
    return resultados

# Execução principal
def main():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, "comentarios.csv")
        df = pd.read_csv(csv_path)

        if "comentario" not in df.columns:
            print("Erro: o arquivo CSV deve conter uma coluna chamada 'comentario'.")
            return

        comentarios = df["comentario"].dropna().tolist()
        client = authenticate_client(AZURE_ENDPOINT, AZURE_KEY)
        resultados = analisar_sentimentos(client, comentarios)

        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv("resultados_sentimentos.csv", index=False)
        print("Análise concluída. Resultados salvos em 'resultados_sentimentos.csv'.")

    except FileNotFoundError:
        print("Erro: arquivo 'comentarios.csv' não encontrado.")
    except HttpResponseError as e:
        print(f"Erro na API: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
