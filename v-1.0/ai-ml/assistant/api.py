import json
from bson import ObjectId, json_util
from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Connect to MongoDB using URI from .env
mongo_uri = getenv('MONGO_URI')
mongo_database = getenv('MONGODB_DB_NAME')

client = MongoClient(mongo_uri)
db = client[mongo_database]
collection = db["empty_coll"]

@app.route('/test', methods=['GET'])
def test_connection():
    try:
        # Try a simple command to check connection
        client.admin.command('ping')
        return jsonify({"message": "MongoDB connection successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get-all', methods=['GET'])
def get_all():
    try:
        colls = db.list_collection_names()
        data: list = []
        for col in colls:
            res = db[col].find_one()
            data.append(res)
        data = json.loads(json_util.dumps(data))
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/get/<id>', methods=['GET'])
def get_data(id: str):
    try:
        colls = db.list_collection_names()
        data: list = []
        for col in colls:
            res = db[col].find_one({'userId': ObjectId(id)})
            data.append({f'{col}': res})
        data = json.loads(json_util.dumps(data))
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
