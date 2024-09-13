#problem link-->> https://leetcode.com/problems/merge-two-binary-trees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1 , node2):
            if (not node1 and node2) or (not node1 and not node2):
                return 1
            if node1 and not node2:
                return 2
            if node1 and node2:
                node2.val = node1.val + node2.val
            res =  dfs(node1.left , node2.left)
            if res == 2:
                node2.left = node1.left
            res = dfs(node1.right , node2.right)
            if res == 2:
                node2.right = node1.right

        a = dfs(root1 , root2)
        if a == 2:
            return root1
        return root2
        


