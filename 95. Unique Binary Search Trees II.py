# problem link-->> https://leetcode.com/problems/unique-binary-search-trees-ii/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def dfs(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            
            temp = []
            for i in range(start, end + 1):
                lefttrees = dfs(start, i - 1)
                righttrees = dfs(i + 1, end)
                for leftnode in lefttrees:
                    for rightnode in righttrees:
                        node = TreeNode(i)
                        node.left = leftnode
                        node.right = rightnode
                        temp.append(node)
            return temp
        
        return dfs(1, n)
        
