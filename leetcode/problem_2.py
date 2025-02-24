"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=0):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def add_two_numbers(self, l1, l2):
        dummy = Node()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.value if l1 else 0
            val2 = l2.value if l2 else 0
            total = val1 + val2 + carry
            carry = total//10
            current.next = Node(total%10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


    def create_linked_list(self, elements):
        dummy = Node()
        current = dummy
        for num in elements:
            current.next = Node(num)
            current = current.next
        return dummy.next

    def print_list(self, head):
        result = []
        while head is not None:
            result.append(head.value)
            head = head.next

        print(result)



my_linked_list = LinkedList()
l1 = my_linked_list.create_linked_list([2, 4, 3])
l2 = my_linked_list.create_linked_list([5, 6, 4])

total = my_linked_list.add_two_numbers(l1, l2)
# print(total)
my_linked_list.print_list(total)
#
# my_linked_list.print_list(l2)


