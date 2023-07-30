from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def root():
    return "Test successful"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6363))
    app.run(port=port)

