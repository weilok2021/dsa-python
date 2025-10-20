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
    def __init__(self):
        self.__first = None
        self.__size = 0
    

    def get_first(self):
        return self.__first
    

    def set_first(self, node):
        if node == None or isinstance(node, Node):
            self.__first = node
        else:
            raise ValueError("First node of linked list must be none or a node")
    

    def is_empty(self):
        return self.get_first() is None
    

    def size(self):
        return self.__size
    

    def push_front(self, value):
        # Initialize new first node, then point it's next to the old first node or None 
        first_node = Node(value, self.get_first())
        # Set this new first node to be the first
        self.set_first(first_node)





                
    

    


