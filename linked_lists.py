class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node | None = None

    def __str__(self):
        return f"{self.value}"
        

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current_item = self.head
        for _ in range(index):
            current_item = current_item.next
        return current_item
    
    def set_value(self, index, value):
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        return False
        
    
    def pop(self):
        current = self.head
        if self.head is None:
            return None
        if self.head is self.tail:
            popped_item = self.head
            self.head = None
            self.tail = None
            return popped_item
        while current.next is not self.tail:
            current = current.next
        popped_item = current.next
        current.next = None
        self.tail = current
        self.length -= 1
        return popped_item
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        node = self.get(index - 1)
        # current_item = self.head
        # for _ in range(index - 1):
        #     current_item = current_item.next
        if node is not None:
            new_node.next = node.next
            node.next = new_node
            self.length += 1
            return True
        return False
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        previous = self.get(index - 1)
        current = previous.next
        previous.next = current.next
        current.next = None
        self.length -= 1
        return current
    
    def pop_first(self):
        if self.head is None:
            return None
        if self.head is self.tail:
            popped_item = self.head
            self.head = None
            self.tail = None
            return popped_item
        popped_item = self.head
        self.head = self.head.next
        popped_item.next = None
        self.length -= 1
        return popped_item
    
    def reverse(self):
        current = self.head
        self.head = self.tail
        self.tail = current
        next = current.next
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
# my_linked_list.insert(1, 1)
my_linked_list.print_list()
my_linked_list.reverse()
# print(my_linked_list.remove(1), '\n')
# my_linked_list.append(3)
# my_linked_list.append(4)
# print(my_linked_list.set_value(0, 3))
# print(my_linked_list.get(1))
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
my_linked_list.print_list()
# print(my_linked_list.head.value)
# print(my_linked_list.tail.value)

