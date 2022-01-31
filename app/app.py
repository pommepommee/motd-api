from flask import Flask
from flask import jsonify
import sys
import os

app = Flask(__name__)
_APP_PORT = os.getenv("APP_PORT")
_MESSAGE = os.getenv("APP_MESSAGE")
print(_APP_PORT, _MESSAGE)

@app.route('/')
def index():
    msg = {"message": _MESSAGE}
    return jsonify(msg)

def main():
    app.run(debug=True, host="0.0.0.0", port=_APP_PORT)

if __name__ == '__main__':
    main()
