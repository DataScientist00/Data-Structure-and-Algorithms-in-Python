# problem link-->> https://leetcode.com/problems/distribute-coins-in-binary-tree/description/?envType=daily-question&envId=2024-05-18

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(cur):
            if not cur:
                return [0,0] # [size , coins]

            l_size , l_coins = dfs(cur.left)
            r_size , r_coins = dfs(cur.right)

            size = 1 + l_size + r_size
            coins = cur.val + l_coins + r_coins
            nonlocal res
            res += abs(size - coins)
            return [size , coins]
        dfs(root)
        return res
        
