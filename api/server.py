from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from detoxify import Detoxify

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def get_toxicity():
    data = request.json
    if not data or not 'sentence' in data.keys():
        return Response('Sentence required', status=400)
    toxicity = Detoxify('original').predict(data['sentence'])
    for key, value in toxicity.items():
        toxicity[key] = str(round(value*100, 2)) + '%'
    return jsonify(toxicity)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
