# problem link-->> https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        for i in range(k-1):
            temp = temp.next

        left = temp
        right = head
        while temp.next:
            temp = temp.next
            right = right.next
        left.val , right.val = right.val , left.val
        return head






        
