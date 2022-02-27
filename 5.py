##5 Add new attributes inside countries which is number of people (find it on Wikipedia)

    col.update_one({'Name': 'USA'}, {'$set': {'Population': 330000000}})
    col.update_one({'Name': 'Morocco'}, {'$set': {'Population':25000000}})
    col.update_one({'Name': 'Norway'}, {'$set': {'Population': 10000000}})
    col.update_one({'Name': 'Canada'}, {'$set': {'Population': 37000000}})
    col.update_one({'Name': 'India'}, {'$set': {'Population': 1400000000}})
    col.update_one({'Name': 'China'}, {'$set': {'Population': 14000000000}})
