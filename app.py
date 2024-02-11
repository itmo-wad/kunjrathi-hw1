from operator import index
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about.css')
def about_css():
    return send_from_directory(os.path.join(app.root_path, 'static'),'about.css')

if __name__ == "__main__":
    app.run(debug=True, port=7000)
