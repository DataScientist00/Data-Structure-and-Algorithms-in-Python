# problem link-->> https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        dummy = head
        temp = head
        head = head.next
        while head:
            value = math.gcd(temp.val , head.val)
            temp.next = ListNode(value , head)
            temp = head
            head = head.next
        return dummy



        
