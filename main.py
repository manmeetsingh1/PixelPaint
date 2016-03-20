
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/holup')
def holup():
    return render_template('holup.html')

if __name__ == '__main__':
    app.run(debug=True)
