from flask import Flask, jsonify, request 


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def get_all_todos(): 
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    try:
       
        if position < 0 or position >= len(todos):
            return jsonify({"msg": f"Error: La posición {position} está fuera de rango."}), 404
            
        print(f"Eliminando la tarea en la posición: {position}")
        todos.pop(position)
        
    except Exception as e:
       
        print(f"Ocurrió un error al eliminar: {e}")
        return jsonify({"msg": "Error interno del servidor al eliminar la tarea"}), 500
        
    
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)