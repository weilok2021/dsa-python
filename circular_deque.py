from ctypes import *
import math

class DynamicArray:
    def __init__(self):
        # creates primitive C array
        self._capacity = 16
        self._array = (c_int * self._capacity)()  # allocate C array of 16 integers
        self._size = 0

        self._end = 0
        print(self._array)
    

    # getter of size
    def size(self):
        # use _size to refer to the instance variable size
        return self._size


    # getter of capacity    
    def capacity(self):
        return self._capacity
    

    def is_empty(self):
        return self.size() == 0
    

    def at(self, i):
        exact_pos = (i + math.floor(self._capacity / 2)) % self._capacity
        return self._array[exact_pos]


    def push(self, item):
        # calculate the exact right end position to insert an item (abstractly right end)
        exact_end = (self._end + math.floor(self._capacity / 2)) % self._capacity
        print(f"End: {exact_end}")
        # insert the item at the exact end
        self._array[exact_end] = item
        self._size += 1
        # Increment the end position one to the right
        self._end += 1

    
    def pop(self):
        # remove and return the last item
        curr_end_pos = (self._end-1 + math.floor(self._capacity / 2)) % self._capacity
        print(f"curr position to be removed: {curr_end_pos}")
        last_item = self._array[curr_end_pos]
        self._array[curr_end_pos] = 0
        self._size -= 1
        self._end -= 1
        return last_item

    def __str__(self):
        list_repr = '['
        for i in range(self.capacity()):
            list_repr += str(self._array[i])
            list_repr += ' ' 
        list_repr += ']'
        return list_repr
    

a = DynamicArray()


print(a.size())
a.push(1)
last = a.pop()
last = a.pop()
print(last)
print(a)