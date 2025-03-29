from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
from pathlib import Path
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)

load_dotenv()

app.config['SECRET_KEY'] = 'FLASK_SECRET_KEY'

path = Path(__file__).parent / 'Relatorio_cadop.csv'


df = pd.read_csv(path, sep=';', encoding='latin1', low_memory=False)
df = df.fillna('')


class BasicForm(FlaskForm):
    ids = StringField('Keyword', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = BasicForm()

    # Inicialização das listas vazias
    results = []
    headers = []
    if request.method == 'POST':

        keyword = request.form.get("keyword", "").strip().lower()

        if keyword and not df.empty:
            try:
                
                filtered_df = df[df.astype(str).apply(lambda row: row.str.contains(keyword, case=False, na=False).any(), axis=1)]
                results = filtered_df.values.tolist()
                headers = filtered_df.columns.tolist()
            except Exception as e:
                return f'bad request {e}', 400

    return render_template('index.html', form=form, results=results, headers=headers)

@app.route('/search', methods=['GET'])
def filter_data():
    # Obter o valor do campo de pesquisa utilizando args pois é get 
    keyword = request.args.get("keyword", '').strip().lower()
    
    
    results = []
    headers = []

    if not df.empty and keyword:
        try:
            
            filtered_df = df[df.astype(str).apply(lambda row: row.str.contains(keyword, case=False, na=False).any(), axis=1)]
            
            filtered_df = filtered_df.fillna('')
            
            results = filtered_df.values.tolist()
            headers = filtered_df.columns.tolist()
            
        
        except Exception as e:
            return f'bad request {e}', 400
    else:
        results = []
        headers = []

    return jsonify({'results': results, 'headers': headers})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
