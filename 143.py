'''REORDER LIST
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Function for reversing
    def reverse(self, head):
        prev = None
        current = head
        while current:
            prev, prev.next, current = current, prev, current.next
        return prev
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        fast = head.next
        slow = head
        # Catch the Middle of List (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Cut Middle of list then Reverse it
        rev = self.reverse(slow.next)
        slow.next = None

        while rev:
            h_next = head.next
            r_next = rev.next
            head.next = rev
            rev.next = h_next
            rev = r_next
            head = h_next  
        
        