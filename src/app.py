from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://myproj_db:27017/pythonmongotask"
mongo = PyMongo(app)

from redis import Redis
from rq import Queue
from worker import background_task 


r = Redis(host="myproj_redis", port=6379, db=0)
q = Queue('my_queue', connection=r)

@app.route("/", methods=["GET"])
def index():
    return "Hello from Flask."

@app.route("/new_task", methods=["POST"])
def get_task():
    tarea = request.json["task"]
    if tarea:
        id = mongo.db.tasks.insert_one(
            {'task':tarea, 'type':'cmd'}
        )
        
        job = q.enqueue(background_task, str(id.inserted_id))
        q_len = len(q)
        print(f"Task {job.id} added to queue at {job.enqueued_at}. {q_len} tasks in the queue.")
        response = jsonify({"id":str(id.inserted_id)})

        return response


@app.route("/get_output/<id>", methods=["GET"])
def get_output(id):
    
    output = mongo.db.tasks.find_one({"_id":ObjectId(id)})
    if output:
        return jsonify({"output": str(output["output"])})
    else:
        not_found()

@app.errorhandler(404)
def not_found(error=None):

    response = jsonify({
        "message":"Resource not found: " + request.url,
        "status":404
    })
    response.status_code=404
    return response



if "__name__"=="__main__":
    app.run(debug=True)