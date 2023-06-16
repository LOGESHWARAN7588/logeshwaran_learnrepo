# we using flask library To get the JSON
# For that using [GET, POST] Method
# we using two function
# Print_hello():
# modify_recipe():


from flask import Flask, jsonify, request

app = Flask(__name__)



# Endpoint for /api/printHello
@app.route('/api/printHello', methods=['GET'])
def print_hello():
    return jsonify({'message': 'Hello, World!'})

# Endpoint for /api/modifyRecepie
@app.route('/api/modifyRecepie', methods=['POST'])
def modify_recipe():
       modified_recipe = "idly"
       return jsonify({'modified_recipe': modified_recipe})

if __name__ == '__main__':
    app.run(port=5001)
