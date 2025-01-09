from flask import Flask, request, jsonify, render_template
from bert_classificator import get_breed, get_eng_name

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.json
    text = data.get('text', '')
    result = get_breed(text)
    eng_name = get_eng_name(result)
    return jsonify({'class': result, 'eng_name': eng_name})

if __name__ == '__main__':
    app.run(debug=True)
