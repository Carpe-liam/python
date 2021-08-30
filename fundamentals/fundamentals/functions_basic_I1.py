    #1 create a countdown function that returns a list from num down to 0 as last element
def countdown(num):
    l = []
    for x in range(num,-1,-1):
        l.append(num)
        num = num-1
    return(l)

print(countdown(5))

    #2 create a function that will receive 2 numbers; print the first and return the second
def print_return(list):
    a=list[0]
    b=list[1]
    print(a)
    return(b)

print(print_return([1,2]))

    #3 create a function that accepts a list & returns the sum of the first value in the list plus it's length
def first_plus_length(list):
    a = list[0]
    b = len(list)
    return(a+b)

print(first_plus_length([1,2,3,4,5]))

    #4 create a function that accepts a list and creates a new list containing only the values from the original list that are > than 2nd value
        #print how many values this is & then return the new list; if new list has < 2 elements, function should return false
def vals_greaterThan_second(list):
    newList =[]
    count =0
    for x in range(len(list)):
        if x > list[1]:
            newList.append(x)
            count = count+1
    print(count)
    if len(newList) <2:
        return(False)
    else:
        return(newList)

print(vals_greaterThan_second([5,2,3,2,1,4]))

    #5 create a function that accepts 2 integers as parameters:size&value. should create & return a list whose length is equal to the given size, 
        # and whose values are all the given value.
def length_and_val(size,value):
    l =size
    a =value
    newList =[]
    for x in range(l):
        newList.append(a)
    return(newList)

print(length_and_val(6,2))