# problem link-->> https://leetcode.com/problems/spiral-matrix-iv/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left , right = 0 , n
        top , bottom = 0 , m
        grid = [[-1]*n for _ in range(m)]

        while head:
            # 1. Left to right
            for i in range(left , right):
                if not head:
                    return grid
                grid[top][i] = head.val
                head = head.next
            top += 1

            # 2.top to bottom
            for i in range(top ,bottom):
                if not head:
                    return grid
                grid[i][right-1] = head.val
                head = head.next
            right -= 1

            # 3. right to left
            for i in range(right-1 , left-1 , -1):
                if not head:
                    return grid
                grid[bottom-1][i] = head.val
                head = head.next
            bottom -= 1

            # 4. bottom to top
            for i in range(bottom-1,top-1,-1):
                if not head:
                    return grid
                grid[i][left] = head.val
                head = head.next
            left += 1
        return grid





        
