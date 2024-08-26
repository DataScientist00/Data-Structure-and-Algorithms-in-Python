#problem link-->> https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = 0
        temp = ListNode(0,head)
        left = temp
        right = head
        while right:
            if t >= n:
                left = left.next
            right = right.next
            t +=1
        left.next = left.next.next
        return temp.next
        
        

