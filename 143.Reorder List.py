#problem link-->> https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next
        #find the middle element of the linked list
        while fast and fast.next:
            print(slow.val,fast.val)
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
      
        #reverse the second half of the linked list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
          
        #merge both of them
        first , second = head , prev
        while second:
            temp1 , temp2 =first.next , second.next
            first.next = second
            second.next = temp1
            first ,second = temp1 , temp2 

            
        
