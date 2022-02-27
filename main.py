import pymongo as pymongo

def print_hi(name):
    print(f'Hi, {name}')

def connectdb():
    client = pymongo.MongoClient("mongodb+srv://mohamad:1731997@cluster0.img42.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    col = db["countries"]
    continents = db["continents"]

    print(db.list_collection_names())

    countries = db.countries

    for country in countries.find():
        print(country['name'])


