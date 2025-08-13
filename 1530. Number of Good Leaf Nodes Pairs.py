# problem link-->> https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.pairs = 0
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            l = dfs(node.left)
            r = dfs(node.right)

            for a in l:
                for b in r:
                    if a+b <= distance:
                        self.pairs += 1
            all_list = l + r
            return [d+1 for d in all_list ]

        dfs(root)
        return self.pairs
        
