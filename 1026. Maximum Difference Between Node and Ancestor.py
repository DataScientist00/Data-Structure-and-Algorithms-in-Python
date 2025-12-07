# problem link-->> https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node , minn , maxx):
            if not node:
                return abs(maxx - minn)

            minn = min(minn , node.val)
            maxx = max(maxx , node.val)
    
            left = dfs(node.left , minn , maxx)
            right = dfs(node.right , minn , maxx)
            return max(left, right)

        return dfs(root , root.val , root.val)
        
