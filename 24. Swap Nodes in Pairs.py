#problem link-->> https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        dummy = ListNode(-1,head)
        prev = dummy
        while first and first.next:
            second = first.next
            third = first.next.next
            second.next = first
            first.next = third
            prev.next = second

            prev = first
            first = third
        return dummy.next


        
