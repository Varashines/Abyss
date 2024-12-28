# Put and Delete HTTP Verbs
#  Working with API's - JSON

from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id":1, "name":"Teju", "Day":"26-04-2024"},
    {"id":2, "name":"Vara", "Day":"04-01-2024"}
]

@app.route('/')
def home():
    return "Welcome to do list app"

@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>',methods = ['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    else:
        return jsonify(item)

@app.route('/items',methods = ['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not found"})
    new_item ={
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "Day": request.json["Day"]
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route('/items/<int:item_id>', methods = ['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    elif not request.json:
        return jsonify({"error": "Request body must be JSON"})
    item['name'] = request.json.get('name',item['name'])
    item['Day'] = request.json.get('Day', item['Day'])
    return jsonify(item)

@app.route('/items/<int:item_id>', methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result":"Item Deleted"})


if __name__ == '__main__':
    app.run(debug=True)
