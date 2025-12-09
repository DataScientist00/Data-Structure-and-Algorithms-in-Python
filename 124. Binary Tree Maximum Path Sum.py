#problem link-->>> https://leetcode.com/problems/binary-tree-maximum-path-sum/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -2000
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            left_accha = node.val + left
            right_accha = node.val + right
            teeno_accha = node.val + right + left
            ans = max(ans , left_accha , right_accha , teeno_accha , node.val)
            return max(node.val , left_accha , right_accha)

        dfs(root)
        return ans
