num1 = 42 # variable declaration, int
num2 = 2.3 # variable declaration, float
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, str
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list declaration - array of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary declaration of objects
fruit = ('blueberry', 'strawberry', 'banana') # tuple declaration - tuple of strings
"""
    End of the declarations
"""
print(type(fruit)) # prints data type of 'fruit' = tuple
print(pizza_toppings[1]) #print pizza toppings at location [1] = Sausage
pizza_toppings.append('Mushrooms') # list.append() method = adds 'Mushrooms' to end of list.
print(person['name']) # prints name of person object = John
person['name'] = 'George' #change person objects name to = George
person['eye_color'] = 'blue'   #add eye color to person = eye color = blue
print(fruit[2]) # print fruit in location [2] of tuple = banana


print(len(string)) #print length of string = 11; 2*5letter words + space



"""
    Start of If/Else Statements
"""
if num1 > 45: #is num1 = 42 > 45 --> no
    print("It's greater") # skipped
else:   # will execute since 42 !> 45
    print("It's lower") #prints str

if len(string) < 5: # len() function; aka length - returns number of items in object. if string char # = 11
    print("It's a short word!") # string =11 so not <5
elif len(string) > 15: #condition satisfied - 11 > 15 true
    print("It's a long word!")  #prints str
else:                       #not needed since satisfied previously; else if both not satisfied will do this
    print("Just right!")    #prints str

for x in range(5):          #in range() function - creates a sequence of nums from 0 to val
    print(x)                #prints each val = 0,1,2,3,4
for x in range(2,5):        #in range() function with a range(start, stop) val. start at 2, stop before 5
    print(x)                #prints each val = 2,3,4
for x in range(2,10,3):     #in range() function - range(start, stop, step) start @ 2, stop before 10, inc by 3
    print(x)                #prints each val = 2,5,8

x = 0           #declare var x val
while(x < 5):   #this is a while loop, start & run until x > 5
    print(x)    #execution
    x += 1      #increment, loop end

pizza_toppings.pop()    #pops final val of pizza_toppings = "mushrooms"
pizza_toppings.pop(1)   #pops val in pizza_toppings[1] spot = "Sausage"

print(person)               #print person values
person.pop('eye_color')     #removes person objects val - eye color
print(person)               #prints person object - now without eye color

for topping in pizza_toppings:      #start for loop
    if topping == 'Pepperoni':      #if topping (1st topping?) is pepperoni = true then continue (does nothing else; c)
        continue                    # continue means print each time 
    print('After 1st if statement') # print string
    if topping == 'Olives':         #if topping in array pizza_topings is olives;
        break                           # end loop

def print_hello_ten_times():        #def = create and execute function called print_hello_ten_times()
    for num in range(10):           #start for loop, 
        print('Hello')              #print "hello" for each num in the range up to 10 set by for loop

print_hello_ten_times()             #run print_hello_ten_times() again

def print_hello_x_times(x):         #new function
    for num in range(x):            #start for loop
        print('Hello')              #print "hello" for each num in the range of (x) taken by function

print_hello_x_times(4)              #run print_hello_ten_times() with x =4 so 4 "hellos" printed

def print_hello_x_or_ten_times(x = 10):     #new function with declaring a x=10
    for num in range(x):                    #start for loop to x which is 10
        print('Hello')                      #print "hello" for each val of x 0-9 (so 10 times)

print_hello_x_or_ten_times()                #run print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)               #run print_hello_x_or_ten_times() again with 4 so only 4 

"""
Bonus section
"""

#print(num3)                         # variable not defined 
#num3 = 72                           # declare int val of 72 for num3
#fruit[0] = 'cranberry'              # tuple object does not support this should be
#print(person['favorite_team'])      # key error - favorite team DNE
#print(pizza_toppings[7])            # out of range - there are not 8 values in pizza_toppings
#    print(boolean)                  # unexpected indent
#fruit.append('raspberry')           # can't append fruit since it is a tuple
#fruit.pop(1)                        # can't pop fruit