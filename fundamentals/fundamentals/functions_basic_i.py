    # prediction = 5
#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

    # prediction = function undefined
#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

    # prediction = 5; can't use 2 returns as the 1st ends function
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

    # prediction = return 5; why did you do this twice in a row?
#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

    # prediction = print 5; also prints none because i'm assuming calling a function with a variable works but there's no value associated with it. 
#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

    #prediction = 8;
        #prints = 3,5 error ; functions do not return a value to be added
#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

    #prediction = 25; they are trasnformed to strings so it's really "2""5" with no space so 25
#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

    #prediction = 100, 10
#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

    # prediction = 7, 14, 21 =-> 7+14=21
#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

    # prediction = 8
#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

    # prediction = 500,500,300,500
#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

    # prediction = 500,500,300,300
        #doesn't actually change b=500
#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

    # prediction = 500,500,300,300
#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

    # prediction = 1,3,2
#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

    # prediction = 1,3,5,10
#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)