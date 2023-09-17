# A tiny sample Flask app for testing with K8s

from flask import Flask
import pymongo
from kubernetes import client, config
import base64

# Get kubernetes secrets for mongo username/password
# This is really bad.. probably shouldn't be using the root user :)
config.load_incluster_config()
v1 = client.CoreV1Api()
mongo_secrets = v1.read_namespaced_secret("mongodb-secret", "my-namespace").data

# setup Mongo client
client = pymongo.MongoClient("mongodb://mongodb-service.default.svc.cluster.local", username=base64.b64decode(mongo_secrets['mongo-root-username']).decode("ascii"), password=base64.b64decode(mongo_secrets['mongo-root-password']).decode("ascii"))

app = Flask(__name__)

# This one lets me know if I did anything right..
@app.route("/")
def hello_world():
    return "<p>This is a Hello World application</p>"


# Access the Mongo table and get all user's names, return them in a string
# This is the saddest code I've ever written...
@app.route("/users")
def get_users():
    db = client["TestDB"]
    col = db["users"]
    
    cursor = col.find({})
    
    result = ""
    for document in cursor:
        result += document['name']
    
    return result



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)