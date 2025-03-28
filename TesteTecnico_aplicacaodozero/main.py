from flask import Flask, render_template, request, jsonify
import pandas as pd
from pathlib import Path
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import json

app = Flask(__name__)

secret_key = os.urandom(32)

app.config['SECRET_KEY'] = secret_key

path = Path(__file__).parent / 'Relatorio_cadop.csv'

df = pd.read_csv(path, sep=';', encoding='latin1')

class BasicForm(FlaskForm):
    ids = StringField('Keyword', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = BasicForm()

    # Inicialização de lista vazias para depois os dados filtrados no DataFrame serem armazenados aqui
    results = []
    headers = []

    if request.method == 'POST':
        keyword = request.form.get("keyword", "").strip().lower()

        keyword_json = json.dumps({'keyword': keyword})

        if keyword and not df.empty:
            # Caso a keyword bata com algo dentro do csv e o df não seja vazio (ou seja, o proprio csv) eles são filtrados e armazenados nas listas anteriormente feitas 

            filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(), axis=1)]
            results = filtered_df.values.tolist()
            headers = filtered_df.columns.tolist()

    return render_template('index.html', form=form, results=results, headers=headers)


@app.route('/search', methods=['GET'])
def filter_data():
    keyword = request.form.get('keyword', '').strip().lower()

    if not df.empty:
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(), axis=1)]
        results = filtered_df.values.tolist()
        headers = filtered_df.columns.tolist()
        return jsonify({'results': results, 'headers': headers})
    return jsonify({'results': [], 'headers': []})
    


if __name__ == '__main__':
    app.run(debug=True)
