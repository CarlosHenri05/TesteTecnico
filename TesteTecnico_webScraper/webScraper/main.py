import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

pasta_pdfs = "pdfs_baixados"
os.makedirs(pasta_pdfs, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


def baixar_pdf(url_pdf, nome_arquivo):
  resposta = requests.get(url_pdf, headers=HEADERS, stream= True)
  try:
    if resposta.status_code == 200:  # verificar se o código de retorno HTTP get é ok
      caminho_arquivo = os.path.join(pasta_pdfs, nome_arquivo)
      with open(caminho_arquivo, "wb") as arquivo:
        for chunk in resposta.iter_content(1024):
          arquivo.write(chunk)
      print(f" PDF salvo: {nome_arquivo}")
  except:
    print(f"Pdf não salvo: {nome_arquivo}")


resposta = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(resposta.text, "html.parser")

pdf_links = []
for link in soup.find_all("a", href=True): # Todos elementos html <a> e que possuam um link href
  if link["href"].endswith(".pdf"):
    pdf_links.append(link["href"])

pdf_links = pdf_links[1:3] # Baixar e salvar na lista apenas os 2 primeiros pdfs encontrados na pagina

for i, pdf_url in enumerate(pdf_links): # fazer uma iteração chave-valor 
  baixar_pdf(pdf_url, f"documento_{i+1}.pdf") # salvar documento utilizando o indice da chave

# Criar arquivo zip com os PDFS

zip_filename = "arquivos_pdfs.zip"
with ZipFile(zip_filename,"w") as zipf: 
  for arquivo in os.listdir(pasta_pdfs):
    zipf.write(os.path.join(pasta_pdfs, arquivo), arquivo)

print(f"Arquivos compactados no dirétorio: {zip_filename}")







