thing = [4,2,7,1,5,6,8,9,3,0]

def insertion_sort(list):
    print(list)
    #take first number and compare it to the first one and flip if needed
    for i in range(1, len(list)):
        key = list[i]
        a = i-1
        print(f'in for loop ~ (i)index @ {i} ={key} ~  a={a} = index(i-1) {list[a]}')
        print('#'*30)
        while a >=0 and key < list[a]:
            print(f"if key(list[i])~ |{key}| < |{list[a]}| ~ list[a]")
            list[a+1] = list[a]
            print(f"SWAP ---> list[a+1]-{list[a+1]} = list[a]-{list[a]}")
            a -=1
            print(f' ~~~~ and a= {a}')
        list[a+1] = key
        print(f'now list[a+1] ->{list[a+1]} = {key} <-- key')
        print(list)
        print('+'*60)
        print('+'*60)


insertion_sort(thing)