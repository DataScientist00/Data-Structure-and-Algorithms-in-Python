#problem link-->> https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        if fast.next == None:
            return True
        else:
            #Find the middle element
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            prev = None
            #Reverse Half of the LL
            while slow:
                forward = slow.next
                slow.next = prev
                prev = slow
                slow = forward
            start = head
            #Compare both half
            while prev:
                if start.val != prev.val:
                    return False
                start = start.next
                prev = prev.next
            return True





        
