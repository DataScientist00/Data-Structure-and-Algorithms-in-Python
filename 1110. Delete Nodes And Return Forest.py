# problem link-->> https://leetcode.com/problems/delete-nodes-and-return-forest/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        def dfs(node):
            if not node:
                return None
            nonlocal res
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)
            if node.val in to_delete:
                if node.left: res.append(node.left)
                if node.right: res.append(node.right)
                return None
            return node
        res = []
        dfs(root)
        if root.val not in to_delete:
            res.append(root)
        return res
        
