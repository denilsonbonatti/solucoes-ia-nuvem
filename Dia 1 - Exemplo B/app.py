import requests

subscription_key = "????"
endpoint = "??????"  

image_url = "https://30683.cdn.simplo7.net/static/30683/sku/camisetas-longline-masculina-camiseta-longline-masculina-vermelha-lisa--p-1619049734626.jpg"

analyze_url = endpoint + "vision/v3.2/analyze"

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

print("Descrição:", analysis["description"]["captions"][0]["text"])

# Verifica objetos detectados
pessoas_detectadas = [obj for obj in analysis.get("objects", []) if obj["object"].lower() == "person"]
print(f"\nPessoas detectadas: {len(pessoas_detectadas)}")

# Verifica cor dominante
cores_dominantes = analysis.get("color", {}).get("dominantColors", [])
print(f"\nCores dominantes: {cores_dominantes}")

# Verifica tags
tags = [tag["name"] for tag in analysis.get("tags", [])]
print(f"\nTags detectadas: {tags}")

# Verificação simples para hipótese de camisa vermelha
if pessoas_detectadas and ("Red" in cores_dominantes or "Red" in tags):
    print("\nPossivelmente há uma pessoa com camisa vermelha na imagem.")
else:
    print("\nNão foi possível confirmar uma pessoa com camisa vermelha na imagem.")