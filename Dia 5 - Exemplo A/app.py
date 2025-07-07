import os
from openai import AzureOpenAI

endpoint = "???"
model_name = "gpt-4.1"
deployment = "gpt-4.1"

subscription_key = "????"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Eu faço curso no senac de Azure AI. Você acha que este curso será útil para a minha carreira profissional",
        }
    ],
    max_completion_tokens=800,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=deployment
)

print(response.choices[0].message.content)