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

    def insertion_sort(self):
        if self.length < 2:
            return
        
        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None
        
        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next
            
            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
        
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp


    # def insertion_sort(self):
    #     if self.head is None:
    #         return
    #     sorted_list = LinkedList(self.head.value)
    #     unsorted_list = self.head.next
    #     while unsorted_list is not None:
    #         prev_sorted_element = sorted_list.head
    #         sorted_element = sorted_list.head
    #         while sorted_element is not None:
    #             if unsorted_list.value < sorted_element.value:
    #                 new_node = Node(unsorted_list.value)
    #                 if sorted_element is sorted_list.head:
    #                     sorted_list.head = new_node
    #                 else:
    #                     prev_sorted_element.next = new_node
    #                 new_node.next = sorted_element
    #                 break
    #             prev_sorted_element = sorted_element
    #             sorted_element = sorted_element.next
    #         if sorted_element is None:
    #             sorted_list.append(unsorted_list.value)
    #         unsorted_list = unsorted_list.next
    #     self.head = sorted_list.head






my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

