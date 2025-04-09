# 🧠 Bot de Automação de Cadastro de Produtos

Este projeto é um bot em Python que automatiza o processo de preenchimento de formulários web com base em dados de uma planilha `.csv`.

## 🔧 Tecnologias usadas
- Python
- PyAutoGUI
- Pandas
- time

## 🚀 Funcionalidades
- Abre o navegador e acessa o sistema
- Realiza login automaticamente
- Lê dados de produtos a partir de um arquivo CSV
- Preenche formulários com as informações dos produtos
- Envia os dados e repete o processo para todos os produtos

## 📂 Estrutura esperada do CSV
O arquivo `produtos.csv` deve conter as seguintes colunas:
- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs`

## 💻 Como usar
1. Instale as dependências:
```bash
pip install pyautogui pandas
