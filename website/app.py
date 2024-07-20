from flask import Flask, render_template, jsonify
import pandas as pd
import sqlite3

app = Flask(__name__)


def load_data():
    conn = sqlite3.connect('immigration_data.db')
    query = "SELECT * FROM data_2019 LIMIT 10;"  
    data = pd.read_sql(query, conn)
    conn.close()
    return data


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/data')
def data():
    data = load_data()
    return render_template('data.html', tables=[data.to_html(classes='data')], titles=data.columns.values)


@app.route('/')
def home():
    return '<h1>Welcome to GROUP 3 PYTHON DATA ON the Immigration Data Website</h1><p><a href="/about">About</a> | <a href="/data">Data</a></p>'

#if __name__ == '__main__':
    app.run(debug=True)

python app.py


