# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack1 = [root]
        result = []
        while stack1:
            temp = stack1.pop()
            result.append(temp.val)
            if temp.right :
                stack1.append(temp.right)
            if temp.left  :
                stack1.append(temp.left)
        #while result:
        return result
                

        