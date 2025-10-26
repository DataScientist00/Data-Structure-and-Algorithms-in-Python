# problem link-->> https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def count_swaps(arr):
            actual = sorted(arr)
            swaps = 0
            idx = {n:i for i , n in enumerate(arr)}
            for i in range(len(arr)):
                if arr[i] != actual[i]:
                    j = idx[actual[i]]
                    arr[i] , arr[j] = arr[j] , arr[i]
                    idx[arr[j]] = j
                    swaps += 1
            return swaps

        q = deque([root])
        res = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += count_swaps(level)
        return res
        
