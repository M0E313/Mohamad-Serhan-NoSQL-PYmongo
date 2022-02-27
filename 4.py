
##4

continents = continents.find({},{'Name':1, 'countries':{'$slice':4}}).sort("Name")
    for FourCountry in continents:
        print(FourCountry)