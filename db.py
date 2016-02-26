from pymongo import MongoClient

client = MongoClient()
db = client.friends_watch

def add_person(person_name):
    if get_person(person_name):
        return False

    db.people.insert({'name': person_name})
    return True

def get_person(person_name):
    cursor = db.people.find({'name': person_name})
    return [person for person in cursor]

def get_people():
    cursor = db.people.find({})
    return [person for person in cursor]
