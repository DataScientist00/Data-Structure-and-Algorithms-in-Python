# problem link-->> https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node , flag , path):
            nonlocal ans
            if not node:
                return 0

            if flag:
                dfs(node.left , not flag , path + 1)
                dfs(node.right , False , 0)
            else:
                dfs(node.right , not flag , path + 1)
                dfs(node.left , True , 0)
            ans = max(ans , path)


        dfs(root , True , 0)
        dfs(root , False , 0)
        return ans

        
