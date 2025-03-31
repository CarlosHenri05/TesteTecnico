## Transformação de dados utilizando Pandas e tabula-py

Este projeto utiliza a biblioteca tabula-py para extrair dados de um arquivo PDF e converter esses dados em um arquivo CSV. Além disso, o script renomeia algumas colunas do DataFrame resultante e compacta o arquivo CSV renomeado em um arquivo ZIP.

### Dependências
Para executar este script, você precisará das seguintes bibliotecas Python:

tabula-py: Utilizada para a leitura de PDFs.

pandas: Utilizada para manipulação de dados.

zipfile: Utilizada para compactação de arquivos.

pathlib: Utilizada para manipulação de caminhos de arquivos.

Você pode instalar as dependências necessárias usando pip:

bash
`pip3 install -r requirements.txt`

### Uso
Preparação do Ambiente:

- Certifique-se de que o arquivo PDF (documento_1.pdf) esteja no mesmo diretório que o script main.py.
- Instale as dependências necessárias.

### Execução do Script:

- Execute o script main.py usando Python:

- bash
- python main.py
### Saída:

O script irá gerar três arquivos:

documento_1.csv: Contém os dados extraídos do PDF.

documento_renomeado.csv: Versão renomeada do arquivo CSV anterior.

documento_csv.zip: Arquivo ZIP contendo o arquivo documento_renomeado.csv.

### Renomeação de Colunas
O script renomeia as colunas "OD" e "AMB" para "Seg.Odontológica" e "Seg.Ambulatorial", respectivamente.

### Compactação do Arquivo
Após a renomeação, o arquivo CSV é compactado em um arquivo ZIP chamado documento_csv.zip.
