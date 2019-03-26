from flask import Flask, g, render_template, url_for
from flask_bootstrap import Bootstrap

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'pickle'

bootstrap = Bootstrap(app)



@app.route('/')
def index():
    return render_template('landing.html')
		

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)