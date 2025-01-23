#problem link-->> https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummynode = ListNode(0 , head)

        prevleft , curr = dummynode , head
        for i in range(left -1):
            prevleft , curr = curr , curr.next
        
        prev = None
        for i in range(right - left + 1):
            tempnext = curr.next
            curr.next = prev
            prev , curr = curr , tempnext

        prevleft.next.next = curr
        prevleft.next = prev
        return dummynode.next
            
        
