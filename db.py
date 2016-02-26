from pymongo import MongoClient

client = MongoClient()
db = client.friends_watch

def add_person(person_name):
    if get_person(person_name):
        return 'person "%s" already exists' % person_name

    db.people.insert({'name': person_name})
    return True

def get_person(person_name):
    cursor = db.people.find({'name': person_name})
    try:
        return cursor[0]
    except:
        return None

def get_people():
    cursor = db.people.find({})
    return [person for person in cursor]

def add_media(media_name, media_length, people):
    if get_media_by_name(media_name):
        return 'media "%s" already exists' % media_name

    db.media.insert({
        'name': media_name,
        'length': media_length,
        'want-to-watch': people
    })
    return True

def get_media(media_length, people):
    cursor = db.media.find({
        'length': {'$lte': media_length},
        'want-to-watch': {'$all': people}
    })
    return [x for x in cursor]

def get_media_by_name(media_name):
    cursor = db.media.find({'name': media_name})
    try:
        return cursor[0]
    except:
        return None
