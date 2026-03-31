class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next
            fast = fast.next
            slow = slow.next
        return slow
    
    def has_loop(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            if fast is slow:
                return True
        return False
    
    def remove_duplicates(self):
        previous = None
        current = self.head
        seen_items = set()
        
        while current is not None:
            if current.value in seen_items:
                previous.next = current.next
            else:
                previous = current
            seen_items.add(current.value)
            current = current.next

    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current is not None:
            num = num * 2 + current.value
            current = current.next
        return num


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""