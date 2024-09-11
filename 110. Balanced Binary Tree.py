#problem link-->> https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node: return (0 , True)
            a = dfs(node.left)
            b = dfs(node.right)
            check =  abs(a[0]-b[0]) <= 1 and a[1] and b[1]
            return (1 + max(a[0],b[0]) , check)
            
        
        return dfs(root)[1]
        

        
