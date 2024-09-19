from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# with open('tasks.json','r') as f:
#     tasks = json.load(f)

mongo_uri = os.environ.get('MONGO_URI','mongodb://localhost:27017')
client = MongoClient(mongo_uri)
db = client['tododb']
tasks_collection = db['tasks']

def task_serializer(task):
    return {
        '_id': str(task['_id']),
        'task': task
    }


@app.route('/list', methods=['GET'])
def list_tasks():
    tasks = list(tasks_collection.find({},{'_id': 0}))
    return jsonify(tasks)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.json.get('task')
    if new_task:
        task_id = tasks_collection.count_documents({})+1
        task = {'id':task_id, 'task': new_task, 'completed': False}
        tasks_collection.insert_one(task)
        return jsonify(task_serializer(task)), 201
    return jsonify({"error": "No task provided"}), 400

@app.route('/complete', methods=['POST'])
def complete_task():
    task_id = request.json.get('id')
    task = tasks_collection.find_one({"id":task_id},{'_id':0})
    if task:
        tasks_collection.update_one({"id":task_id},{"$set": {"completed":True}})
        task['completed'] = True
        return jsonify(task_serializer(task))
    return jsonify({"error": "Task not found"}), 404

@app.route('/incomplete', methods=['POST'])
def incomplete_task():
    task_id = request.json.get('id')
    task = tasks_collection.find_one({"id":task_id},{'_id':0})
    if task:
        tasks_collection.update_one({"id": task_id},{"$set":{"completed":False}})
        task['completed'] = False
        return jsonify(task_serializer(task))
    return jsonify({"error":"Task not found"}), 404

@app.route('/dump' , methods=['GET'])
def dump():
    tasks = list(tasks_collection.find({},{'_id': 0}))
    return jsonify({"message": f"{len(tasks)} tasks stored in MongoDB"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
    