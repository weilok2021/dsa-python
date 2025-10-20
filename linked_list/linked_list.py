class Node:
    def __init__(self, datum, next=None):
        # Data for this node
        self.__data = datum
        # reference to next node
        self.__next = next


    # Getter for this node's data
    def get_data(self):
        return self.__data


    # Setter for this node's data
    def set_data(self, datum):
        self.__data = datum


    # Getter to the reference to next node
    def get_next(self):
        return self.__next


    # Setter to the reference to next node
    def set_next(self, node):
        # reference to next node must be type node or None
        if node is None or isinstance(node, Node):
            self.__next = node
        else:
            raise ValueError("The next must be None or reference to another node!")


    # Test if this is the last node in the chain
    def is_last(self):
        return self.get_next() is None


    # String representation of this node
    def __str__(self):
        return str(self.get_data())
    

# LinkedList implementation without tail pointer
class LinkedList:
    # def __init__(self):
    #     self.head = Node("HEAD")
    #     self._size = 0
    
    # # Getter that returns self._size instance variable
    # def size(self):
    #     return self._size
    

    # def is_empty(self):
    #     return self.size() == 0


    # def push_front(self, value):
    #     # Initialize new node to be pushed
    #     node = Node(value) 
    #     # IF this is an empty linkedlist, point head to the new node
    #     if self.is_empty():
    #         self.head.next = node
    #     else:
    #         # Point this new node to first node, which is head
    #         node.next = self.head.next
    #         self.head.next = node
    #     self._size += 1

    
    def __str__(self):
        temp = self.head
        ll_repr = ""
        while temp != None and not self.is_empty():
            ll_repr += f"{temp.value} -> "
            temp = temp.next
        ll_repr += "NULL"
        return ll_repr


                
    

    


