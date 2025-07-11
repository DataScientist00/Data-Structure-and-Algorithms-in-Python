# problem link-->> https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        i = 0
        while i < a-1:
            curr = curr.next
            i += 1
        head = curr
        while i <= b:
            curr = curr.next
            i += 1
        head.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = curr
        return list1
        
