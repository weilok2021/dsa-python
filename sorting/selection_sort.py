# What this algorithm does?

# Initialize smallest element to arr[i] for every ith iteration
# Find the smallest element in the inner for loop
# Then swap this smallest element with current ith element 

def selection_sort(arr):
    for i in range(len(arr)):
        smallest_elem = arr[i]
        smallest_index = i
        for j in range(i, len(arr)):
            if arr[j] < smallest_elem:
                smallest_elem = arr[j]
                smallest_index = j
        # swap the current element with the smallest element in this iteration
        temp = arr[i] 
        arr[i] = smallest_elem 
        arr[smallest_index] = temp 
    return arr


print(selection_sort([]))

    