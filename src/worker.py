import time
import os

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://myproj_db:27017/")
db = client["pythonmongotask"]

#tengo que crear conexion con mongo

def background_task(id):
    print(f"starting task {id}...")
    time.sleep(5)
    input = db.tasks.find_one({"_id":ObjectId(id)})
    tarea = input["task"] #esto se lo tengo que pasar a os
    # print(tarea)
    # esta tomando bien ls
    stream = os.popen(tarea)
    output = stream.read()
    # esta tomando bien output
    db.tasks.update_one({"_id":ObjectId(id)}, {"$set":{
            "output":output
        }})
    print (f"task {tarea} is finished.")

    return "everything ok"