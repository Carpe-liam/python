#1 - print 0-150
for x in range(151):
    print(x)

#2 - print multiples of 5 from 5-1000
for x in range(5, 1001, 5):
    print(x)

#3 print integers 1-100; if divisible by 5 - print"coding" instead; if divisible by 10 - print"Coding Dojo"
for x in range(1,101):
    if x % 5 == 0 and x%10 != 0:
        print("Coding")
    elif x % 10 == 0 and x%5 ==0: 
        print("Coding Dojo")
    else:
        print(x)

#4 Add odd integers from 0-500,000 and print final sum
sum =0
for x in range(0,5000001):
    sum = sum +x
print(sum) #returns 12500002500000

#5 print positive numbers starting a 2018, counting down by 4
for x in range(2018,0,-4):
    if x%2==0:
        print(x)

#6 set 3 variables: lowNum, highNum & mult. print only integers that're a multiple of mult.
lowNum =2
highNum =9
mult=3
for x in range(lowNum,highNum+1):
    if x%mult==0:
        print(x)