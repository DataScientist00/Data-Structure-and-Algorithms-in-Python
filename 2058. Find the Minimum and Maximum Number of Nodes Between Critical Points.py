# problem link-->> https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        prev1 = prev.next
        prev2 = prev1.next
        if not prev2 or not prev1 or not prev:
            return [-1,-1]
        idx = []
        count = 0
        minD = float('inf')
        while prev1.next:
            count += 1
            if prev.val < prev1.val and prev1.val > prev2.val:
                idx.append(count)
            elif prev.val > prev1.val and prev1.val < prev2.val:
                idx.append(count)
            prev = prev.next
            prev1 = prev1.next
            prev2 = prev2.next
        print(idx)
        for i in range(1,len(idx)):
            diff = idx[i] - idx[i-1]
            minD = min(minD ,diff)
        return [-1 , -1] if len(idx) < 2 else [minD , abs(idx[0] - idx[-1])]
        
        
