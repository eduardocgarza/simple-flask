from dotenv import load_dotenv
load_dotenv()
from flask_cors import CORS
from flask import Flask
from src.api.get_messages import get_messages
from src.api.get_root import get_root
from src.api.get_status import get_status


app = Flask(__name__)
CORS(app)


@app.route("/")
def root():
    return get_root()


@app.route("/status")
def status():
    return get_status()


@app.route("/messages")
def messages():
    return get_messages()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
