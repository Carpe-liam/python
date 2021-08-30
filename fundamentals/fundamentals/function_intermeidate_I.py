"""    
    1 Update values in Dictionaries and Lists
"""
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

    #1 
def chang_xVal(myList,num):
    for i in range(len(myList)):
        for j in range(len(myList[i])):
            if(myList[i][j] ==num):
                myList[i][j] = 15
    print(myList)

chang_xVal(x,10)

    #2
def chng_lName(myList):
    for d in myList:
        if(d['last_name'] == 'Jordan'):
            d['last_name'] = 'Bryant'
    print(myList)
    return myList

chng_lName(students)

    #3
def chng_fName(myDict,nName):
    for l in myDict:
        for x in range(len(myDict[l])):
            if(myDict[l][x]=='Messi'):
                myDict[l][x] = nName
    print(myDict)
    return(myDict)

chng_fName(sports_directory, 'Andre')

    #4 -list w/ dict
def chng_zVal(aList, nVal):
    for i in range(len(aList)):
        print(aList[i])
        for x,y in aList[i].items():
            print(x,y)
            if(y == 20):
                aList[i].update({'y' : nVal})
        print(aList)
        return aList

chng_zVal(z, 30)

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