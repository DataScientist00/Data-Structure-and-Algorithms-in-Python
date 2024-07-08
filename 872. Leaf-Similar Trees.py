#problem link-->> https://leetcode.com/problems/leaf-similar-trees/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,leaf):
            if not node:
                return True
            if not node.left and not node.right:
                leaf.append(node.val)
                return
            dfs(node.left,leaf)
            dfs(node.right,leaf)
        
        a=[]
        b=[]
        dfs(root1,a)
        dfs(root2,b)
        return a==b

        

        
        
