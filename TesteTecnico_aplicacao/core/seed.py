from core import db, app
import pandas as pd
from pathlib import Path

archive_path = Path('Relatorio_cadop.csv')

# def seed_data():
#   with app.app_context():
#     with open(archive_path,newline='', encoding='utf-8' ) as csvfile:
#       df = pd.read_csv(csvfile)

print(archive_path)

