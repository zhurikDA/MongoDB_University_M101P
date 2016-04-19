import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

def avg_city_pop():
    # get a handle to the blog database
    db=connection.test
    collection = db.zips
    try:
        cursor = collection.aggregate(
            [
                { "$match": {"state": {"$in": ["CA", "NY"]}}},
                { "$group": { "_id": { "state": "$state", "city": "$city" }, "pop": { "$sum": "$pop" } } }
                ,{ "$match": {"pop": {"$gt": 25000}}}
                ,{ "$group": { "_id": "", "avgCityPop": { "$avg": "$pop" } } }                
            ])        
        for document in cursor:
            print(document)
    except Exception as e:
        print ("Unexpected error:", type(e), e) 
        
avg_city_pop()