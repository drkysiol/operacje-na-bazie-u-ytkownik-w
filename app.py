from flask import Flask, jsonify, request
from collections import defaultdict

app = Flask(__name__)
users_db = defaultdict(dict)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([{"id": id, **user} for id, user in users_db.items()])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    if id in users_db:
        return jsonify(users_db[id])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    next_id = max(users_db.keys()) + 1 if users_db else 1
    users_db[next_id] = new_user
    return jsonify(new_user), 201

@app.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    if id in users_db:
        partial_user = request.json
        users_db[id].update(partial_user)
        return '', 204
    else:
        return jsonify({"error": "User not found"}), 400

@app.route('/users/<int:id>', methods=['PUT'])
def replace_user(id):
    if id in users_db:
        users_db[id] = request.json
        return '', 204
    else:
        return jsonify({"error": "User not found"}), 400

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id in users_db:
        del users_db[id]
        return '', 204
    else:
        return jsonify({"error": "User not found"}), 400

if __name__ == '__main__':
    app.run(debug=True)