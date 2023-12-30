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
        # if self.head is None:
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # def get(self, index):
    #     if index < 0 or index >= self.length:
    #         return None
    #     else:
    #         temp = self.head
    #         for _ in range(index):
    #             temp = temp.next
    #         return temp

    # The above get_method is same as it was for the singly_linked_list and it will work perfectly
    # fine for doubly_linked_list as well, but we can make this get_method more efficient for
    # doubly_linked_list.

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp


my_doubly_linked_list = DoublyLinkedList(1)

my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

print(my_doubly_linked_list.get(1))
print(my_doubly_linked_list.get(2))
