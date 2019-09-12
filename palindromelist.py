class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self,sequence):
        #prepends item of lists into linkedlists
        self.head = None
        for item in sequence:
            node = Node
            node.next = self.head
            self.head = Node

    def palindrome_list(self):
        #returns 1 if linked list is palindrome else 0
        node = self.head
        fast = node
        prev = None
        is_palindrome = True

        while fast and fast.next: 
            fast = fast.next.next
            temp = node.next   #reverse elemets of first half of list
            node.next = prev
            prev = node
            node = temp

        if fast:  # in case of odd num elements
            tail = node.next
        else:    # in case of even num elements
            tail = node


        while prev and is_palindrome:
            # compare reverse element and next half elements          
            if prev.val == tail.val:
                tail = tail.next
                prev = prev.next
                is_palindrome = True
            else:
                is_palindrome = False
                break

        if is_palindrome :
            return 1
        else :
            return 0


# # Test Cases
# tests = [
#     ([], True),
#     ([1], True),
#     ([1, 1], True),
#     ([1, 2], False),
#     ([3, 7, 3], True),
#     ([3, 7, 4], False),
#     ([6, 3, 7, 3, 6], True),
#     ([7, 8, 6, 3, 7, 3, 6, 8, 7], True),
#     ([7, 8, 6, 3, 7, 4, 6, 8, 7], False),
# ]
# for inp, expected in tests:
#     res = Solution(inp).palindrome_list()
#     if res != expected:
#         print("%s: %d != %d" % (inp, res, expected))