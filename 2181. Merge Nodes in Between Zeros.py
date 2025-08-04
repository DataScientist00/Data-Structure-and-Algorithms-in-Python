# problem link-->> https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        total = 0
        ans = []
        while head.next != None:
            total += head.val
            if head.val == 0:
                ans.append(total)
                total  = 0
            head = head.next
        ans.append(total)
        for i in range(1,len(ans)):
            dummy.next = ListNode(ans[i] , None)
            dummy = dummy.next
        return temp.next

        
