def find_smallest(arr):
    smallest = arr[0]
    smallest_i = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_i = i
    return smallest_i


def selection_sort(arr):
    new_arr = []
    while arr:
        smallest_i = find_smallest(arr)
        new_arr.append(arr[smallest_i])
        arr.pop(smallest_i)
    return new_arr


print(selection_sort([3,1,2]))

    