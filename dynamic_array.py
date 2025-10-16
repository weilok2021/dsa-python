from ctypes import *
import math

class DynamicArray:
    def __init__(self, capacity = 16):
        # creates primitive C array
        self._capacity = capacity
        self._array = (c_int64 * self._capacity)()  # allocate C array of 16 integers
        self._size = 0


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
        if i >= self.size() or i < 0:
            raise IndexError("Index out of bound")
        return self._array[i]


    def push(self, item):
        # array reach its capacity
        if self.size() == self.capacity():
            # resize to double the size
            self.resize(self.capacity() * 2)

        self._array[self.size()] = item
        self._size += 1

    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty array")
        # when popping an item, if the size is 1/4 of capacity, resize to half
        if self.size() <= (1 / 4 * self.capacity()):
            self.resize(self.capacity() // 2)

        last_elem = self._array[self.size() - 1]
        # remove this element
        self._array[self.size() - 1] = 0
        self._size -= 1
        return last_elem
    

    def resize(self, new_capacity):
        double_capacity_array = (c_int * new_capacity)()  # allocate new capacity of C array 
        # copy all elements from currect array in to new larger array
        for i in range(self.size()):
            double_capacity_array[i] = self._array[i]
        self._capacity = new_capacity
        self._array = double_capacity_array


    def __str__(self):
        list_repr = '['
        for i in range(self.capacity()):
            list_repr += str(self._array[i])
            list_repr += ' ' 
        list_repr += ']'
        return list_repr
    

a = DynamicArray()
for i in range(5000):
    a.push(i+1)

print(a.capacity())

for j in range(2953):
    a.pop()
