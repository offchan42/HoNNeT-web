from flask import Flask, render_template
from honnet import load

app = Flask(__name__)
model = load()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
