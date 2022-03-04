from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from detoxify import Detoxify

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def get_toxicity():
    data = request.json

    # Error if no sentence sent by client
    if not data or not 'sentence' in data.keys():
        return Response('Sentence required', status=400)

    # Usage of detoxify model with client sentence
    toxicity = Detoxify('original').predict(data['sentence'])
    # Get percentage for each result returned by model
    for key, value in toxicity.items():
        toxicity[key] = str(round(value*100, 2)) + '%'

    return jsonify(toxicity)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
