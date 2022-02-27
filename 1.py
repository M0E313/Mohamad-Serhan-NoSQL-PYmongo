
##1
    var = input("enter your word")
    myquery = { "name": { "$regex": str(var) } }

    mydoc = col.find(myquery)

    for x in mydoc:
        print(x)

