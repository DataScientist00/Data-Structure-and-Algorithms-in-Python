#problem link-->> https://leetcode.com/problems/partition-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return None
        start = head
        dummy1 = ListNode(-1,None)
        temp1 = dummy1
        dummy2 = ListNode(-2 ,None)
        temp2 = dummy2
        while start:
            if start.val < x:
                temp1.next = start
                temp1 = temp1.next
            else:
                temp2.next = start
                temp2 = temp2.next
            start = start.next
        temp2.next = None
        temp1.next = dummy2.next
        return dummy1.next

