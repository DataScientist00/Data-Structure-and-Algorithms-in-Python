#problem link-->>>> https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node , maxx):
            if not node: return
            if node.val >= maxx:
                nonlocal count
                count += 1
            dfs(node.left , max(node.left.val if node.left else 0 ,maxx))
            dfs(node.right , max(node.right.val if node.right else 0 ,maxx))
                    

        dfs(root , root.val)
        return count
