# problem link-->> https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            row_max = q[0].val
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                row_max = max(row_max , node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(row_max)
        return res
