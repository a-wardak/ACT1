from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
    except ValueError:
        return jsonify({'błąd': 'Wprowadź wartości liczbowe'}), 400

    suma = a + b
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        'prediction': prediction,
        'features': {
            'a': a,
            'b': b,
            'suma': suma
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
