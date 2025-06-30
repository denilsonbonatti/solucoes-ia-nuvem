import requests

# Substitua pelos seus dados do portal
subscription_key = "????"
endpoint = "?????"  

# URL do primeiro exemplo
image_url = "https://static.wixstatic.com/media/9c0dec_17b23fd31e7c43a9b87e91ca737724e6~mv2_d_3008_1688_s_2.jpg/v1/fill/w_558,h_431,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/9c0dec_17b23fd31e7c43a9b87e91ca737724e6~mv2_d_3008_1688_s_2.jpg"

# URL da API com o caminho /vision/v3.2/analyze
analyze_url = endpoint + "vision/v3.2/analyze"

# Parâmetros da análise
params = {
    "visualFeatures": "Categories,Description,Tags,Objects,Color",
    "language": "pt"
}

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

data = {
    "url": image_url
}

response = requests.post(analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()

analysis = response.json()

# Exibe a descrição da imagem
print("Descrição:", analysis["description"]["captions"][0]["text"])

# Lista objetos encontrados
print("\nObjetos detectados:")
for obj in analysis.get("objects", []):
    print(f" - {obj['object']} (confiança: {obj['confidence']:.2f})")
