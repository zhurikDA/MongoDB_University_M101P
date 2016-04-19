import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

def find_most_friquent_author():
    # get a handle to the blog database
    db = connection.test
    collection = db.grades
    try:
        cursor = collection.aggregate(
                     [
                       { "$unwind": "$scores"}
                       ,{ "$match": {"scores.type": {"$nin": ["quiz"]}}}
                       ,{ "$group": {"_id": { "class_id": "$class_id", "student_id": "$student_id" }, 
                                            "avgStudentScore": { "$avg": "$scores.score" } } },
                       { "$group": {"_id": "$_id.class_id" , 
                                           "avgClassScore": { "$avg": "$avgStudentScore" } } },                
                       { "$sort": { "avgClassScore": -1 } }
                       ,{ "$limit": 1 }
                     ])        
        for document in cursor:
            print(document)
    except Exception as e:
        print ("Unexpected error:", type(e), e) 
        
find_most_friquent_author()