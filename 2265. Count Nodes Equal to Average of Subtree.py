# problem link -->> https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return (0,0)
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            avg = (left_val[0] + right_val[0] + node.val) // (left_val[1] + right_val[1] + 1)
            if avg == node.val:
                ans += 1
            return ( left_val[0] + right_val[0] + node.val,left_val[1] + right_val[1] + 1)

        dfs(root)
        return ans
        
