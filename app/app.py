from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<flag>')
def flag(flag):
    if flag is 'cdc{url_injection}':
        return "<h1>%s</h1>" % flag
    else:
        return render_template('welcome.html')