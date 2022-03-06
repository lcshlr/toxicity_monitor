from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from detoxify import Detoxify
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Summary, Counter

import time

app = Flask(__name__)
CORS(app)

metrics = PrometheusMetrics(app)
REQUESTS = Counter('toxicity_api_requests_total', 'Total number of requests')
EXCEPTIONS = Counter('toxicity_api_exceptions_total', 'Total number of 400.')
LATENCY = Summary('toxicity_api_latency_seconds', 'Latency of the server')

@app.route('/', methods=['POST'])
def get_toxicity():
    REQUESTS.inc()
    start = time.time()
    data = request.json

    # Error if no sentence sent by client
    if (not data or not 'sentence' in data.keys()) or data['sentence'] == 'test_raise_exception':
        EXCEPTIONS.inc()
        LATENCY.observe(time.time() - start)
        return Response('Sentence required', status=400)

    # Usage of detoxify model with client sentence
    toxicity = Detoxify('original').predict(data['sentence'])
    # Get percentage for each result returned by model
    for key, value in toxicity.items():
        toxicity[key] = str(round(value*100, 2)) + '%'

    LATENCY.observe(time.time() - start)
    return jsonify(toxicity)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
