import requests

# Substitua pelos seus dados do portal
subscription_key = "1diLLIYGFfuQfkelbOUGb97LsseTEEp7F4XzcwA73gFtRrDmsrwNJQQJ99BGACYeBjFXJ3w3AAAFACOGyQZG"
endpoint = "https://azure-aula-senac.cognitiveservices.azure.com/"  

# URL do primeiro exemplo

#Foto 1: https://website2021-live-e3e78fbbd3cc41f2847799-7c49c59.divio-media.com/filer_public_thumbnails/filer_public/73/52/7352020b-b331-47f5-8405-3d114bf0f28a/types-of-meetings.png__1200x630_q90_crop_subject_location-420%2C304_subsampling-2_upscale.png
#Foto 2: https://portaledicase.com/wp-content/uploads/2023/03/cachorros-scaled.jpg
#Foto 3: https://a-static.mlcdn.com.br/800x560/conjunto-feminino-alfaiataria-blusa-shorts-cinto-linho-top-verde-naromi/shoporiginal/a1n5-987-p/a03ca82d666115b26cdb86dc730e32e6.jpeg
#Foto 4: https://a-static.mlcdn.com.br/800x560/conjunto-feminino-alfaiataria-linho-blusa-regata-short-cinto-amarelo-naromi/shoporiginal/a4n3-1152-p/a8b93f3abcf2c6658aaab342f449c0e3.jpeg

image_url = "https://a-static.mlcdn.com.br/800x560/conjunto-colete-cropped-e-saia-vermelho-fina-moca/bellamadamme/11f4c6f4ccef11eeade44201ac185040/6757212b244b0b7dafa976b5b3415c6e.jpeg"

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
