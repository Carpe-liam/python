# python code below!
arra = [3,1,6,7,5]

def bubble_sort(arr):
    for i in range(len(arr)):
        print(i)
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1], arr[i]
            return arr
    print(arr)
        

bubble_sort(arra)