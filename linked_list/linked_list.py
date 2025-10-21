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
    

    def inc_size(self):
        self.__size += 1
    

    def dec_size(self):
        self.__size -= 1


    def value_at(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Index out of bound")
        first = self.get_first()
        first_index = 0
        while first_index < index:
            first = first.get_next()
            first_index += 1
        return first.get_data()


    def push_front(self, value):
        if isinstance(value, Node):
            raise TypeError("push_front expects a value, not a Node object")
        # Initialize new first node, then point it's next to the old first node or None 
        new_first_node = Node(value, self.get_first())
        # Set this new first node to be the first
        self.set_first(new_first_node)
        self.inc_size()

    
    def pop_front(self):
        if self.is_empty():
            raise Exception("Can't remove front from an empty list")
        first_node = self.get_first()
        first_data = first_node.get_data()
        self.set_first(first_node.get_next())
        self.dec_size()
        return first_data
    

    # push the item to the end of the linked list
    def push_back(self, value):
        new_last_node = Node(value)
        # if this is an empty list, point the first reference to this new last node
        if self.is_empty():        
            self.set_first(new_last_node)
        else:
            old_last_node = self.get_first()
            # Traverse the list to get the last node
            while old_last_node.get_next() != None:
                old_last_node = old_last_node.get_next()
            # point the next of old last node to new last node
            old_last_node.set_next(new_last_node)
        self.inc_size()
    

    # Pop the item out from the end of linked list
    def pop_back(self):
        if self.is_empty():
            raise Exception("Can't pop back for an empty list")
        # IF there's only one element in the list, this element is the last element
        elif self.size() == 1:
            last_data = self.back()
            self.set_first(None)
            self.dec_size()
            return last_data
        else:
            # get the last node value to be returned later
            last_data = self.back()
            second_last_node = self.get_first()
            # traverse list to get the second last node
            while second_last_node.get_next().get_next() != None:
                second_last_node = second_last_node.get_next()
            # point the next of second last node to None
            second_last_node.set_next(None)
            self.dec_size()
            return last_data
    
    
    def back(self):
        if self.is_empty():
            raise Exception("No back for an empty list")
        last_node = self.get_first()
        while last_node.get_next() != None:
            last_node = last_node.get_next()
        return last_node.get_data()


    def front(self):
        if self.is_empty():
            raise Exception("No front for an empty list")
        first_node = self.get_first()
        return first_node.get_data()

    
    def __str__(self):
        list_repr = ""
        if not self.is_empty():
            first = self.get_first()
            while first:
                list_repr += f"[{first.get_data()}] -> "
                first = first.get_next()
        list_repr += "None"
        return list_repr


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)

ll = LinkedList()
ll.push_front(3)
ll.push_front(2)
ll.push_front(1)
print(ll.front())
print(ll.size())
print(ll)



                
    

    


