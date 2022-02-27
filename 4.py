
##4 Send back the fourth countries of a continent by alphabetic order

continents = continents.find({},{'Name':1, 'countries':{'$slice':4}}).sort("Name")
    for FourCountry in continents:
        print(FourCountry)
