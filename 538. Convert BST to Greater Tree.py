#problem link-->> https://leetcode.com/problems/convert-bst-to-greater-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running_sum = 0
        def dfs(node):
            if not node:
                return
            
            nonlocal running_sum
            dfs(node.right)
            temp = node.val
            node.val += running_sum
            running_sum += temp
            dfs(node.left)
        dfs(root)
        return root
            

        
