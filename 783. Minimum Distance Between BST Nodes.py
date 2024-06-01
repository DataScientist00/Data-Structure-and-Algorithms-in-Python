#problem link ---->>>> https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.currentnode = None
        self.minimum = float("inf")

        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            if self.currentnode:
                self.minimum = min(self.minimum,node.val - self.currentnode.val)
            
            self.currentnode = node
            dfs(node.right)
            
        dfs(root)
        return self.minimum






        
        
