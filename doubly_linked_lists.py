class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def pop_first(self):
        if self.head is None:
            return None
        item = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            item.next = None
        self.length -= 1
        return item
    
    def pop(self):
        if self.head is None:
            return None
        if self.head is self.tail:
            removed_item = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed_item
        removed_item = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        removed_item.prev = None
        self.length -= 1
        return removed_item
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        before = self.get(index - 1)
        item_to_remove = before.next
        next = item_to_remove.next
        before.next = next
        next.prev = before
        item_to_remove.next = None
        item_to_remove.prev = None
        self.length -= 1
        return item_to_remove

        
        
        

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)

my_doubly_linked_list.insert(1,2)

# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(2)


# print('Get node from first half of DLL:')
# print(my_doubly_linked_list.get(1).value)

# print('\nGet node from second half of DLL:')
# print(my_doubly_linked_list.get(2).value)

# print(my_doubly_linked_list.pop_first())

# print(my_doubly_linked_list.pop())