class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

# LinkedList implementation without tail pointer
class LinkedList:
    def __init__(self):
        self.head = Node("HEAD")
        self._size = 0
    
    # Getter that returns self._size instance variable
    def size(self):
        return self._size
    

    def is_empty(self):
        return self.size() == 0


    def push_front(self, value):
        # Initialize new node to be pushed
        node = Node(value) 
        # IF this is an empty linkedlist, point head to the new node
        if self.is_empty():
            self.head.next = node
        else:
            # Point this new node to first node, which is head
            node.next = self.head.next
            self.head.next = node
        self._size += 1

    
    def __str__(self):
        temp = self.head
        ll_repr = ""
        while temp != None and not self.is_empty():
            ll_repr += f"{temp.value} -> "
            temp = temp.next
        ll_repr += "NULL"
        return ll_repr


                
    

    


