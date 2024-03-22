'''PALINDROME LINKED LIST
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.'''
class Solution(object):
    def isPalindrome(self, head):
        reversed_node=None
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            reversed_node, reversed_node.next, slow=slow, reversed_node, slow.next
        if fast:
            slow=slow.next
        while reversed_node and reversed_node.val==slow.val:
            slow=slow.next
            reversed_node=reversed_node.next
        return not reversed_node
        