# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(current_index, len(arr)):
            # checks to see if the item at index j is less than item at index of current_minimum
            if arr[j] < arr[current_minimum]:
                # If the item at j is less than the item at current_minimum, current_minimum will now be j
                current_minimum = j
        
        # After we go through the entire array we swap the item at current_minimum with the current_index
        arr[current_minimum], arr[current_index] = arr[current_index], arr[current_minimum]


    return arr

print(selection_sort([78, 248, 61, 233, 11, 212, 142, 91, 197, 203, 192, 111, 234, 66, 178, 38, 73, 188, 211, 114])) 
             


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i] > alist[i + 1]:
                temp = arr[i]
                arr[i] = arr[i+ 1]
                arr[i + 1] = temp

    return arr

print(bubble_sort([54,26,93,17,77,31,44,55,20]))
print(bubble_sort([78, 248, 61, 233, 11, 212, 142, 91, 197, 203, 192, 111, 234, 66, 178, 38, 73, 188, 211, 114]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr