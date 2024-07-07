#problem link-->> https://leetcode.com/problems/range-sum-of-bst/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        self.range_sum = 0
        self.fn(root,low,high)
        return self.range_sum

    def fn(self,node,low,high):
        if node:

            if low <= node.val <= high:
                self.range_sum += node.val
            if node.val > low:
                self.fn(node.left,low,high)

            if node.val < high:
                self.fn(node.right,low,high)


        
