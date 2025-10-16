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


    def at(self, index):
        if index >= self.size() or index < 0:
            raise IndexError("Index out of bound")
        return self._array[index]


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
    

    def insert(self, index, item):
        if index > self.size() or index < 0:
            raise IndexError("Index out of bound")

        # array reach its capacity
        if self.size() == self.capacity():
            # resize to double the size
            self.resize(self.capacity() * 2)
        

        for i in range(self.size(), index, -1):
            #[1,2,3,4,5]
            # call a.insert(0, 10)
            # when i = 5: [1,2,3,4,5,5]
            # when i = 4: [1,2,3,4,4,5]
            # ...
            # when i = 1: [1,1,2,3,4,5]
            
            # shift current element one index to the right
            self._array[i] = self._array[i - 1]

        # insert item into this empty position (the old elements are shifted to the right)
        self._array[index] = item        
        self._size += 1
    

    def prepend(self, item):
        self.insert(0, item)


    def resize(self, new_capacity):
        double_capacity_array = (c_int * new_capacity)()  # allocate new capacity of C array 
        # copy all elements from currect array in to new larger array
        for i in range(self.size()):
            double_capacity_array[i] = self._array[i]
        self._capacity = new_capacity
        self._array = double_capacity_array


    def delete(self, index):
        if self.is_empty():
            raise IndexError("Can't delete item from empty array")
        if index >= self.size() or index < 0:
            raise IndexError("Index out of bound") 
        
        # when deleting an item, if the size is 1/4 of capacity, resize to half
        if self.size() <= (1 / 4 * self.capacity()):
            self.resize(self.capacity() // 2)

        # remove element at index position
        self._array[index] = 0
        # Shift any element at the right of self._array[index] one position to the left
        for i in range(index, self.size() - 1):
            self._array[i] = self._array[i + 1]
        
        self._size -= 1
    

    def remove(self, item):
        # for i in range(self.size(), -1, -1):
        #     if self._array[i]  == item:
        #         self.delete(i)
        i = 0
        # [ 7, 7, 7]
        while i < self.size():
            if self._array[i] == item:
                # don't increment i, recheck this index
                self.delete(i)
            else:
                i += 1


    def to_list(self):
        """Return the current elements as a regular Python list."""
        return [self._array[i] for i in range(self._size)]


    def __str__(self):
        list_repr = '[ '
        for i in range(self.size()):
            list_repr += str(self._array[i])
            list_repr += ' ' 
        list_repr += ']'
        return list_repr
    

b = DynamicArray()
for _ in range(3):
    b.push(7)
b.push(1)
b.push(2)
b.push(3)
b.remove(7)
b.remove(3)
print(b.to_list(), b.size())

