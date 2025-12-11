# problem link-->> https://leetcode.com/problems/maximum-width-of-binary-tree/description/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root , 1)])
        ans = 1

        while q:
            first_idx = q[0][1]
            for i in range(len(q)):
                node  , idx = q.popleft()
                if node.left:
                    q.append((node.left , 2*idx))
                if node.right:
                    q.append((node.right , 2*idx+1))

            ans = max(ans , idx - first_idx + 1)
        return ans
        
