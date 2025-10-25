# problem link--> https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(node):
            if not node:
                return None
            q = deque()
            q.append(node)
            i = 0
            while q:
                if i & 1:
                    l = 0 
                    r = len(q)-1
                    while l < r:
                        q[l].val , q[r].val = q[r].val , q[l].val
                        l += 1
                        r -= 1
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                i += 1

        bfs(root)
        return root

            
        
