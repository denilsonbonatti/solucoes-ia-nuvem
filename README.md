# 🔍 Projetos com Azure Computer Vision API

Este repositório contém dois projetos desenvolvidos em Python que utilizam a **Azure Computer Vision API** para analisar imagens e realizar tarefas com base em detecção de objetos, descrição automática e análise de cores.

## 📁 Projetos

### 1. 🖼️ Analisador de Imagens com Interface Gráfica (Tkinter)

**Descrição:**  
Um aplicativo desktop que permite ao usuário selecionar uma imagem do seu computador e obter:
- A descrição gerada automaticamente pela IA da Azure
- Lista de objetos detectados com grau de confiança
- Interface gráfica simples usando `Tkinter`

**Funcionalidades adicionais do exercício proposto:**
- Gera automaticamente três variações de legendas:
  - Legenda original da API
  - Legenda para redes sociais
  - Legenda para acessibilidade

---

### 2. 👕 Detector de Camiseta e Análise de Estilo via URL

**Descrição:**  
Um script que envia a URL de uma imagem para a API da Azure e retorna:
- A descrição da imagem
- Objetos detectados (com ênfase em pessoas)
- Cores dominantes
- Tags relacionadas
- Avaliação se há ou não uma pessoa com camiseta vermelha

**Funcionalidades adicionais do exercício proposto:**
- O script gera **sugestões de combinações de roupas** com base nas cores detectadas.
- Pode ser facilmente adaptado para uso em lojas virtuais ou apps de recomendação de moda.


---

## ☁️ Requisitos

- Conta Azure com serviço **Computer Vision** criado
- Chave de assinatura (Subscription Key)
- Endpoint do serviço

---
