from flask import Flask, json, jsonify, request


app = Flask(__name__)

big_data = {
    'data_values': []
}


@app.route('/')
def my_first_function():
    return jsonify({
        'key': 'value'
    })
    

@app.route('/<number>', methods=['GET'])
def return_index(number):
    try:
        return jsonify(big_data['data_values'][int(number)])
    except IndexError:
        response = jsonify({
            'value not found': 'Try again'
        })
        response.status_code = 404
        return response
    
    
@app.route('/queries/test', methods=['GET'])
def return_query():
    arg = request.args.get('number', default=10, type=int)
    return jsonify({'The arg is': arg})
    
    
@app.route('/post-request', methods=['POST'])
def post_request():
    data = request.json
    big_data['data_values'].append(data)
    return jsonify(big_data)
    

if __name__ == '__main__':
    app.run()