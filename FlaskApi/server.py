from flask import Flask
from core.models.searching import *
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)