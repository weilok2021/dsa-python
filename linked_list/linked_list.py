class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList implementation without tail pointer
class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    # Getter that returns self._size instance variable
    def size(self):
        return self._size
    

    def empty(self):
        return self.size() == 0

    
    
    


