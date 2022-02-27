    
##7

for continents in col.find({
        'Name':
            {'$regex': 'u', '$options': 'i'}, 'Population': {'$gt': 100000}
    }
    ).sort("population"):
        print(continents['Name'], continents['Population'])
