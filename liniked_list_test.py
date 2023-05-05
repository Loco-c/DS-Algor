# Node class 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_node:
    def __init__(self, value):
        new_node = Node(value)
        self.value =  value
        self.head = new_node
        self.tail = new_node 
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None 
        for _ in range(self.length):
            after = temp.next
             
    
ll= Linked_node(1)
print(ll.print_list())



 prev = None
        current = head
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev