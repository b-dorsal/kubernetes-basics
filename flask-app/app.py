# A tiny sample Flask app for testing with K8s

from flask import Flask
import pymongo
import os
import base64

username = os.getenv('PYMONGO_USERNAME')
password = os.getenv('PYMONGO_PASSWORD')

# setup Mongo client
client = pymongo.MongoClient("mongodb://mongodb-service.flask-app-ns.svc.cluster.local", username=username, password=password)

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
    
    result = "<ul>"
    for document in cursor:
        result += f'<li>{document["name"]}</li>'
    result += "</ul>"
    return result



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)