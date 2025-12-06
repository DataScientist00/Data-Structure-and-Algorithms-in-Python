# problem link-->> https://leetcode.com/problems/add-one-row-to-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(node , d):
            if d == depth-1:
                if node:
                    left_temp = node.left
                    right_temp = node.right
                    node.left = TreeNode(val,left_temp,None)
                    node.right = TreeNode(val,None,right_temp)
                return
            if not node:
                return

            dfs(node.left , d+1)
            dfs(node.right,d+1)


        if depth == 1:
            return TreeNode(val,root,None)
        dfs(root , 1)
        return root
        
        
