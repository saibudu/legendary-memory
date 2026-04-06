from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# database sementara (list)
todo = []

# 🔹 GET - ambil semua data
@app.route("/todo", methods=["GET"])
def get_todo():
    return jsonify({
        "data": todo
    })


# 🔹 POST - tambah data
@app.route("/todo", methods=["POST"])
def add_todo():
    data = request.json

    if not data or "task" not in data:
        return jsonify({"error": "task harus ada"}), 400

    new_todo = {
        "id": len(todo) + 1,
        "task": data["task"]
    }

    todo.append(new_todo)

    return jsonify({
        "message": "berhasil ditambah",
        "data": new_todo
    })


# 🔹 PUT (URL) - update pakai ID di URL
@app.route("/todo/<int:id>", methods=["PUT"])
def update_todo_url(id):
    data = request.json

    if not data or "task" not in data:
        return jsonify({"error": "task harus ada"}), 400

    for item in todo:
        if item["id"] == id:
            item["task"] = data["task"]
            return jsonify({
                "message": "berhasil diupdate (URL)",
                "data": item
            })

    return jsonify({"error": "data tidak ditemukan"}), 404


# 🔹 PUT (BODY) - update pakai ID dari body
@app.route("/todo", methods=["PUT"])
def update_todo_body():
    data = request.json

    if not data or "id" not in data or "task" not in data:
        return jsonify({"error": "id dan task harus ada"}), 400

    for item in todo:
        if item["id"] == data["id"]:
            item["task"] = data["task"]
            return jsonify({
                "message": "berhasil diupdate (BODY)",
                "data": item
            })

    return jsonify({"error": "data tidak ditemukan"}), 404


# 🔹 DELETE - hapus data
@app.route("/todo/<int:id>", methods=["DELETE"])
def delete_todo(id):
    for item in todo:
        if item["id"] == id:
            todo.remove(item)
            return jsonify({
                "message": "berhasil dihapus"
            })

    return jsonify({"error": "data tidak ditemukan"}), 404


# 🔥 RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)
