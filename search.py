def sequential_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
        
    return -1

array = [1,2,3,4,5]
target = 3

index = sequential_search(array, target)

if index != -1:
    print("The value was found at index", index)
else: 
    print("The target value was not found in the array")
    