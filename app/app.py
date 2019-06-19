from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flag', methods=['GET', 'POST'])
def flag():
    if request.method == 'POST':
        return 'cdc{good_request}'
    else:
        return 'change your methods'

if __name__=="__main__":
    app.run()