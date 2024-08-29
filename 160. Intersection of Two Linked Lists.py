#problem link-->> https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB
        count1 = count2 = 0
        while temp1:
            count1 += 1
            temp1 = temp1.next
        while temp2:
            count2 +=1
            temp2 = temp2.next
        temp1 = headA
        temp2 = headB
        t = abs(count1 - count2)
        if count1 > count2:
            while t:
                temp1 = temp1.next
                t -= 1
            while temp2:
                if temp1 == temp2:
                    return temp1
                temp1 = temp1.next
                temp2 = temp2.next
        elif count1 < count2:
            while t:
                temp2 = temp2.next
                t -= 1
            while temp1:
                if temp1 == temp2:
                    return temp1
                temp1 = temp1.next
                temp2 = temp2.next
        else:
            while temp1:
                if temp1 == temp2:
                    return temp1
                temp1 = temp1.next
                temp2 = temp2.next
        return None
