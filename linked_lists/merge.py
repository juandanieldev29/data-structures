class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def merge(self, other_list):
        other_head = other_list.head
        dummy = Node(0)
        current = dummy
 
        while self.head is not None and other_head is not None:
            if self.head.value < other_head.value:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other_head
                other_head = other_head.next
            current = current.next
 
        if self.head is not None:
            current.next = self.head
        else:
            current.next = other_head
            self.tail = other_list.tail
 
        self.head = dummy.next
        self.length += other_list.length


    # def merge(self, l2):
    #     if not self.head:
    #         return None
    
    #     dummy = Node(0)
    #     prev = dummy
    #     current_l1 = self.head
    #     current_l2 = l2.head
    
    #     while current_l1 and current_l2:
    #         if current_l1.value < current_l2.value:
    #             prev.next = current_l1
    #             prev = prev.next
    #             current_l1 = current_l1.next
    #         else:
    #             prev.next = current_l2
    #             prev = prev.next
    #             current_l2 = current_l2.next
    #     while current_l1:
    #         prev.next = current_l1
    #         prev = prev.next
    #         current_l1 = current_l1.next
    #     while current_l2:
    #         prev.next = current_l2
    #         prev = prev.next
    #         current_l2 = current_l2.next
    #     self.head = dummy.next
    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""