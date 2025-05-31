# problem link-->> https://leetcode.com/problems/split-linked-list-in-parts/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        output = []
        cur , n = head , 0
        while cur:
            cur = cur.next
            n += 1
        part , left = n//k , n%k
        cur = head
        prev = None

        for _ in range(k):
            output.append(cur)
            for _ in range(part):
                if cur:
                    prev= cur
                    cur = cur.next
            if left and cur:
                prev = cur
                cur = cur.next
                left -= 1
            if prev: prev.next = None
        return output
        
