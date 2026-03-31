class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values)) 

    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current is not None:
            num = num * 2 + current.value
            current = current.next
        return num
    
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
# linked_list.append(1)
result = linked_list.binary_to_decimal()
print(result)