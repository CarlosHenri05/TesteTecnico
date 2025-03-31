# Aplicação Vue.js + Flask

Esta aplicação consiste em um frontend desenvolvido em Vue.js e um backend em Flask que oferece um endpoint `/search` para pesquisa de dados armazenados em um arquivo CSV.

## Tecnologias Utilizadas

- **Frontend:** Vue.js
- **Backend:** Flask (Python)
- **Banco de Dados:** Arquivo CSV
- **Outras bibliotecas:** Pandas, Flask-WTF, Flask-CORS, WTForms, dotenv

## Instalação e Execução

### Backend (Flask)
1. Clone este repositório:
   ```sh
   git clone https://github.com/CarlosHenri05/TesteTecnico.git
   cd TesteTecnico_aplicacaodozero
   ```
2. Crie um ambiente virtual e instale as dependências:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Coloque o arquivo `Relatorio_cadop.csv` na raiz do projeto.
4. Execute a aplicação Flask:
   ```sh
   python main.py
   ```

### Frontend (Vue.js)
1. Acesse a pasta do frontend e instale as dependências:
   ```sh
   cd csv-api
   npm install
   ```
2. Execute o servidor Vue.js:
   ```sh
   npm run serve
   ```

## Endpoints da API

### `GET /search`
Busca dados no CSV filtrando por uma palavra-chave.

**Parâmetros:**
- `keyword` (string) - Palavra-chave para filtrar os dados.

**Resposta:**
```json
{
  "results": [["valor1", "valor2", "valor3"], ...],
  "headers": ["Coluna1", "Coluna2", "Coluna3"]
}
```
![38f7a30e-69ae-42af-a14d-4f865e36184f](https://github.com/user-attachments/assets/b800152d-5ba4-4e3d-b8ba-405f9c15e199)


## Licença
Este projeto está sob a licença MIT.

