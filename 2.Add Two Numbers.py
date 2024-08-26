#problem link-->> https://leetcode.com/problems/add-two-numbers/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = ListNode()
        cur = temp_head
        carry = 0
        while l1 or l2 or carry:
            t1 = l1.val if l1 else 0
            t2 = l2.val if l2 else 0

            #Finding Carry and Value
            t3= t1 + t2 + carry
            carry = t3 // 10
            value = t3 % 10

            #append addition to LL and move to next value
            cur.next = ListNode(value)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return temp_head.next







        
