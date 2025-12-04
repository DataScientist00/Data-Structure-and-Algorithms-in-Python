# problem link -- >> https://leetcode.com/problems/binary-tree-pruning/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val == 0 and  node.left == None and node.right == None:
                return None
            else:
                return node

        return dfs(root)
        
