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