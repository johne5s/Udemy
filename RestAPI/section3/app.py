from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

#static memory of stores
stores =[
    {
        'name':'My Wonderfull Store',
        'items':[
            {
                'name':'My Item',
                'price':15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store<string:item>', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

@app.route('/store<string:name>/item')
def get_item_in_store(name):
    pass

app.run(port=5000)