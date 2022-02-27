
##1 Get all the country where a letter or word given is in the name => for example: FR Fran… 
   
    var = input("enter your word")
    myquery = { "name": { "$regex": str(var) } }

    mydoc = col.find(myquery)

    for x in mydoc:
        print(x)

