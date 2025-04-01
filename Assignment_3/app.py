from flask import Flask, request, jsonify
from score import score
import pickle

app = Flask(__name__)

with open('./Assignment_3/best_model.pkl', 'rb') as file:
  model = pickle.load(file)

@app.route('/test', methods=['GET'])
def test_endpoint():
    """Endpoint for checking if the API is running"""
    return jsonify({
        "message": "Welcome to the scoring API!",
    })

@app.route('/score', methods=['POST'])
def score_endpoint():
    """Endpoint for scoring text"""
    data = request.get_json()
    text = data.get('text', '')
    threshold = float(data.get('threshold', 0.5))
    
    prediction, propensity = score(text, model, threshold)
    
    return jsonify({
        'prediction': "spam" if prediction else "ham",
        'propensity': propensity
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)