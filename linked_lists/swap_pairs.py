class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result
    
    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        first = previous.next
        while first and first.next:
            second = first.next
            previous.next = second
            first.next = second.next
            second.next = first
            previous = first
            first = first.next
        self.head = dummy.next

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
# linked_list.append(5)

linked_list.swap_pairs()

linked_list.print_list()