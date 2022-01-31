from flask import Flask
from flask import jsonify
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('APP_PORT', type=int, help="Application port, default 5000", default="5000")
parser.add_argument('MESSAGE', type=str, help="Message to display")

args = parser.parse_args()

app = Flask(__name__)

@app.route('/')
def index():
    msg = {"message": args.MESSAGE}
    return jsonify(msg)

def main():
    app.run(debug=True, host='0.0.0.0', port=args.APP_PORT)

if __name__ == '__main__':
    main()
