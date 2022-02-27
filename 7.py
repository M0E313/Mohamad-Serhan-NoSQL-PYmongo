    
##7 Get countries which have a ‘u’ in their name and more 100 000 people inside

for continents in col.find({
        'Name':
            {'$regex': 'u', '$options': 'i'}, 'Population': {'$gt': 100000}
    }
    ).sort("population"):
        print(continents['Name'], continents['Population'])
