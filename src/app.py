from flask import Flask, request, jsonify, render_template
from bert_classificator import get_breed

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.json
    text = data.get('text', '')
    result = get_breed(text)
    return jsonify({'class': result})

if __name__ == '__main__':
    app.run(debug=True)
