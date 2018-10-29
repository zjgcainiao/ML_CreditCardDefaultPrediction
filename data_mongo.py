# Dependencies
import pymongo 
import datetime
import json

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.payments_db

# Declare the collection
collection = db.payments_db

# Part I
# A dictionary that represents the document to be inserted
with open('data.json') as f:
    file_data = json.load(f)

collection.insert(file_data)
# Verify results:
#results = db.payments_db.find()
#for result in results:
#    print(result)

#mongoimport --db dbName --collection collectionName --file fileName.json --jsonArray