# problem link-->> https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([(root , 1)])
        total = float('-inf')
        ans = 0
        while q:
            temp_sum = 0
            for i in range(len(q)):
                node , level = q.popleft()
                temp_sum += node.val
                if node.left:
                    q.append([node.left , level+1])
                if node.right:
                    q.append([node.right , level+1])
            if temp_sum > total:
                ans = level
                total = temp_sum
        return ans
