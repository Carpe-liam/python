"""
    2 - Iterate through a list of dictionaries
"""
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    #1
def iterateDictionary(some_list):
    for x in range(len(some_list)):
        print(some_list[x])

#iterateDictionary(students)

"""
    3 - Get values from a list of dictionaries
"""
def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('last_name', students)

"""
    4 - Iterate through a dictionary with list values
"""
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for k, v in some_dict.items():
        n = str(len(some_dict[k]))
        t = k.upper()
        print(n + " " + t)
        for i in v:
            print(i)

printInfo(dojo)