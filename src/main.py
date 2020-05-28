from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world():
    return render_template('main.html', name=None)