
import pymongo

uri = 'mongodb+srv://admin:adminpass@cluster0.7vdrx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'


def get_database(name="None"):
  client = pymongo.MongoClient(uri)

  if name == "None":
    db = client.players
  else:
    db = client.name
  return db

def get_collection(db="None", name="None"):
  if db == "None":
    db = get_database()
    if not name == "None":
      collection = db.name
    else:
      collection = db.list_collection_names()[0]
  else:
    if not name == "None":
      collection = db.name
    else:
      collection = db.list_collection_names()[0]
  return collection

