# problem link-->>>> https://leetcode.com/problems/cousins-in-binary-tree-ii/description/


#--------------double-dfs-------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.hashtable = defaultdict(int)
        self.hashtable[0] = root.val
        def dfs(node , depth):
            if not node:
                return 0
            if node.left:
                self.hashtable[depth] = self.hashtable[depth] + node.left.val
            if node.right:
                self.hashtable[depth] = self.hashtable[depth] + node.right.val
                
            dfs(node.left , depth+1)
            dfs(node.right , depth+1)

        def dfs2(node,depth):
            if not node:
                return 0
            value = self.hashtable[depth]
            if node.left:
                value -= node.left.val
            if node.right:
                value -= node.right.val
            if node.left:
                node.left.val = value
            if node.right:
                node.right.val = value

            dfs2(node.left , depth+1)
            dfs2(node.right , depth+1)

            

            
        dfs(root , 1)
        dfs2(root , 1)
        if root:
            root.val = 0
        return root

