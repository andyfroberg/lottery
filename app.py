from flask import Flask


app = Flask(__name__)


# Routes
@app.route('/')
def home():
    pass


@app.route('drawing')
def drawing():
    pass


