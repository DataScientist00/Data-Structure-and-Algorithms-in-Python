# problem link-->> https://leetcode.com/problems/path-sum-ii/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        temp = []
        def dfs(node):
            if not node:
                return
                    
            temp.append(node.val)
            dfs(node.left)
            dfs(node.right)
            if not node.left and not node.right:
                if sum(temp) == targetSum:
                    ans.append(temp[:])
            temp.pop()

        dfs(root)
        return ans
        
