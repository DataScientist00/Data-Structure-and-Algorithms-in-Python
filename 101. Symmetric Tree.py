# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left , right) :
            # if both child are null
            if not left and not right :
                return True
            # if one side is null but other not so it is not symmetric
            if not left or not right :
                return False
            return (left.val == right.val and dfs(left.left , right.right) and dfs(left.right ,right.left))
        return dfs(root.left,root.right)
        return result
                

        
