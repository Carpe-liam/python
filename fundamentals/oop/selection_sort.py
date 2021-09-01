thing = [4,2,7,1,4,8,9,3,0]

def selection_sort(list):
    for i in range(len(list)):
        print(f'list[i] = {list[i]} at index {i} - iteration~{i}')
        for x in range(len(list)-1):
            print(f"comparing I=val {list[i]} with X=val {list[x]}")
            if list[i] < list[x]:
                list[i], list[x] = list[x], list[i]
                print(f'swapped {list[i]} with {list[x]}')
                print("~"*50)
        print("end of x loop")
        print("+"*23)        
    print(list)        

selection_sort(thing)