#problem link-->> https://leetcode.com/problems/remove-linked-list-elements/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1 , head)
        slow = dummy
        fast = head
        while fast:
            if fast.val == val:
                fast = fast.next
                slow.next = slow.next.next
            else:
                slow=slow.next
                fast=fast.next
        return dummy.next
        
