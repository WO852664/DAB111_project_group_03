from flask import Flask, render_template
import pandas as pd
import sqlite3
import pathlib


base_path = pathlib.Path(r'C:\Users\aranu\OneDrive\Desktop\PYTHON\DAB111_project_group_03\database')
db_name = base_path / 'immigration_data.db'

app = Flask(__name__)

def load_data():
    con = sqlite3.connect(db_name)
    query = "SELECT * FROM data_2019 LIMIT 10;"
    data = pd.read_sql(query, con)
    con.close()
    return data

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    data = load_data()
    # Pass the HTML of the dataframe to the template
    return render_template('data.html', tables=[data.to_html(classes='data', index=False)], titles=data.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
