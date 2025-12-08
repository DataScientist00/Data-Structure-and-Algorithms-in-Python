# problem link-->> https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7

        def total(node):
            if not node:
                return 0
            cumsum = node.val + total(node.left) + total(node.right)
            return cumsum
        total_sum = total(root)

        ans = float('-inf')
        def product(node):
            nonlocal total_sum , ans
            if not node:
                return 0
            temp = node.val + product(node.left) + product(node.right)
            ans = max(ans , temp * (total_sum - temp))
            return temp

        product(root)
        return ans % MOD        
        
