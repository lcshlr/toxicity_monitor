import requests


def test_no_toxic_sentence_is_no_toxic():
    url = 'http://localhost:5000/'
    response = requests.post(url, json={'sentence': 'Hi'})
    toxicity = float(response.json()['toxicity'][:-1])
    print('toxicity', toxicity)
    assert toxicity < 0.5


def test_toxic_sentence_is_toxic():
    url = 'http://localhost:5000/'
    response = requests.post(url, json={"sentence": "It is a big shit"})
    toxicity = float(response.json()['toxicity'][:-1])
    print('toxicity', toxicity)
    assert toxicity > 90
