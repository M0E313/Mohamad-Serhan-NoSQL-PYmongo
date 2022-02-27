##6

    for countries in col.find({}).sort("Population"):
        print(countries['Name'], countries['Population'])