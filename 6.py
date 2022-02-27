##6 Get all the countries order by number of people first the less populated and last the most populated

    for countries in col.find({}).sort("Population"):
        print(countries['Name'], countries['Population'])
