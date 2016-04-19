import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

def find_most_friquent_author():
    # get a handle to the blog database
    db=connection.blog
    collection = db.posts
    try:
        cursor = collection.aggregate(
                     [
                       { "$project": {"_id": 0, "comments": 1}},
                       { "$unwind": "$comments"},
                       { "$group": { "_id": "$comments.author", "total": { "$sum": 1 } } },
                       { "$sort": { "total": 1 } }
                       ,{ "$limit": 1 }
                     ])       
        for document in cursor:
            print(document)
    except Exception as e:
        print ("Unexpected error:", type(e), e) 
        
find_most_friquent_author()