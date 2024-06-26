from pymongo import MongoClient
from bson.son import SON

client = MongoClient("DB_URI")
Database = client['chessbot']
Users = Database['Users']
Events = Database['Events']

def saveNewUser(message):
    userDoc = {
        '_id':message.from_user.id,
        'name':f'''{message.from_user.first_name}''',
        'username':message.from_user.username,
        'strength':0
    }

    tryUser =  Users.find_one({'_id':message.from_user.id})
    if not tryUser:
        Users.insert_one(userDoc)

def addstrength(userid):
    user = Users.find_one({'_id':userid})
    strength = user['strength']
    Users.update({'_id':userid},{'$set':{'strength':strength+1}})

    return strength+1

def delstrength(userid):
    user = Users.find_one({'_id':userid})
    strength = user['strength']
    Users.update({'_id':userid},{'$set':{'strength':strength-1}})

    return strength-1
    
def showstrength(userid):
    user = Users.find_one({'_id':userid})
    strength = user['strength']

    return strength  


def ranking(userid):
    user = Users.find_one({'_id':userid})
    strength = user['strength']

    if int(strength) > 0 and int(strength) < 10:
        rank = "Academy Student Level"

    elif strength >= 10 and strength < 20:
        rank = "Genin Level"

    elif strength >= 20 and strength < 30:
        rank = "Chunin Level"

    elif strength >= 30 and strength < 40:
        rank = "Jounin Level"

    elif strength >= 40 and strength < 50:
        rank = "Special Jounin Level"
        
    elif strength >= 50 and strength < 60:
        rank = "ANBU Level"
        
    elif strength >= 60 and strength < 70:
        rank = "ANBU Level"

    elif strength >= 70 and strength < 80:
        rank = "Kage Level"

    elif strength >= 80 and strength <90:
        rank = "s-Class"

    elif strength >= 90 and strength < 95:
        rank = "SS-Class"

    elif strength >= 95:
        rank = "SSS-Class"

    else:
        rank = "Not Specified"

    return rank

async def getSorted():
    pipeline = [{"$sort":SON([("strength",-1)])}]
    return list(Users.aggregate(pipeline))
    
