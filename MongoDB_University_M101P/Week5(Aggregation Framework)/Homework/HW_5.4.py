import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

def number_of_people():
    # get a handle to the blog database
    db = connection.test
    collection = db.zips
    try:
        cursor = collection.aggregate(
                     [
                       { "$project": {"_id": 0, 
                                      "first_char": {"$substr" : ["$city",0,1]}, 
                                      "pop": 1}}
                       #,{ "$match": {"$or": [{"first_char": {"$type": 1}}, {"first_char": {"$type": 16}}, {"first_char": {"$type": 18}}]}}
                       #,{ "$match": {"first_char": {"$not": {"$type": 2}}}}
                       ,{ "$match": {"first_char": {"$gte": "0", "$lte": "9"}}}
                       ,{ "$group": {"_id": "" , 
                                            "total": { "$sum": "$pop" } } },
                     ])
        #cursor = collection.find({"comments.author": "Tresa Sinha"})        
        for document in cursor:
            print(document)
    except Exception as e:
        print ("Unexpected error:", type(e), e) 
        
number_of_people()