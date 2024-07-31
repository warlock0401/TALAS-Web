from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/trending-topics', methods=['GET'])
def get_trending_topics():
    with open('trending_topics.json', 'r') as f:
        trending_topics = json.load(f)
    return jsonify(trending_topics)


if __name__ == '__main__':
    app.run(debug=True)
