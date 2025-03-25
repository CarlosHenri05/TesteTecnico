# Existe varias APIS feitas para leitura de PDF, porém escolhi a tabula-py pois era mais recomendada em foruns. 
import tabula
import zipfile 
import os
import pandas as pd
from pathlib import Path

p = Path(__file__).with_name("documento_1.pdf")
file_path = p.absolute()

df = tabula.read_pdf(file_path,pages='all')

tabula.convert_into(file_path, "documento_1.csv", output_format='csv', pages='all')


def compress_archive(csv_filename, zip_filename='documento_csv.zip'):
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_filename, arcname=os.path.basename(csv_filename))

        print(f"Arquivo  {csv_filename},compactado com sucesso em {zip_filename}")
    except Exception as e:
        print(f"Erro ao compactar o arquivo: {e}")

panda_df = pd.read_csv("documento_1.csv", on_bad_lines='skip')

renamed_df = panda_df.rename(
    columns={
        "OD" : "Seg.Odontológica",
        "AMB": "Seg.Ambulatorial"
    }
)

renamed_df.to_csv("documento_renomeado.csv", index=False)

compress_archive("documento_renomeado.csv")


