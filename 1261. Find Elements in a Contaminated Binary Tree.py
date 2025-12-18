# problem link-->> https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.stored = set()
        def dfs(node , v):
            if not node:
                return
            node.val = v
            self.stored.add(v)
            if node.left:
                dfs(node.left , 2*v+1)
            if node.right:
                dfs(node.right , 2*v+2)
        dfs(root , 0)
    
    def find(self, target: int) -> bool:
        if target in self.stored:
            return True
        else:
            return False



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
