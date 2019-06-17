from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/flag')
def flag():
    return "<h1>cdc{url_injection}</h1>"