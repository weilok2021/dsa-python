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
        """ Returns element at index position from the array
        """
        if index >= self.size() or index < 0:
            raise IndexError("Index out of bound")
        return self._array[index]


    def push(self, item):
        """ Insert element at the end of array, takes O(1) run time 
        """
        # array reach its capacity
        if self.size() == self.capacity():
            # resize to double the size
            self.resize(self.capacity() * 2)

        self._array[self.size()] = item
        self._size += 1

    
    def pop(self):
        """ Remove element at the end of array, takes O(1) run time
            return the removed element
        """
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
        """ Insert item at index position in the array
        """
        if index > self.size() or index < 0:
            raise IndexError("Index out of bound")

        # array reach its capacity
        if self.size() == self.capacity():
            # resize to double the size
            self.resize(self.capacity() * 2)
        

        for i in range(self.size(), index, -1):            
            # shift current element one index to the right
            self._array[i] = self._array[i - 1]

        # insert item into this empty position (the old elements are shifted to the right)
        self._array[index] = item        
        self._size += 1
    

    def prepend(self, item):
        """ Insert item at 0th position in the array
        """
        self.insert(0, item)


    def resize(self, new_capacity):
        """ resize the original array to new array with new capacity
        """
        new_array = (c_int * new_capacity)()  # allocate new capacity of C array 
        # copy all elements from currect array into new array
        for i in range(self.size()):
            new_array[i] = self._array[i]
        self._capacity = new_capacity
        self._array = new_array


    def delete(self, index):
        """ Remove items at index position from the array
        """
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
        """ Looks for item and removes index holding it (even if in multiple places)
        """
        i = 0
        # [ 7, 7, 7]
        while i < self.size():
            if self._array[i] == item:
                # don't increment i, recheck this index
                self.delete(i)
            else:
                i += 1


    def find(self, item):
        """ Returns first index holding this item,
            IF item doesn't exist in the array, returns -1
        """
        for i in range(self.size()):
            if self._array[i] == item:
                return i
        return -1


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
b.prepend(1)
b.prepend(2)
b.prepend(3)
print(b.to_list(), b.size())

