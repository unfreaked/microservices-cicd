from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def get_products():
    return jsonify([
        {'id': 1, 'name': 'Widget'},
        {'id': 2, 'name': 'Gadget'}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002) 