# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        curr=list1
        i=0
        while i<a-1:
            curr=curr.next
            i+=1
            
        head=curr
        while i<=b:
            curr =curr.next
            i+=1
        head.next=list2

        while list2.next:
            list2=list2.next
        list2.next=curr
        return list1

