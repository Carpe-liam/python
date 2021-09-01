arra = [1,8,5,3,2,0]

def bubble_sort(arr):
    for j in range(len(arr)-1):
        print("\n", f"{'-'*50}, iteration +{j}")
        for i in range(len(arr)-1-j):
            print(f'compare:  {arr[i]} {arr[i+1]}')
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print(f"swapped {arr[i]} ~ {arr[i+1]}")
            else:
                print(f'swap no need for {arr[i]} and {arr[i+1]}')
                print('~'*50)
    print(arr)


bubble_sort(arra)