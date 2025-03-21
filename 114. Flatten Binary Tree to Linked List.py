#problem link-->> https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            lefttail = dfs(root.left)
            righttail = dfs(root.right)
            if root.left:
                lefttail.right = root.right
                root.right = root.left
                root.left = None
            last = righttail or lefttail or root
            return last
        dfs(root)

        #
