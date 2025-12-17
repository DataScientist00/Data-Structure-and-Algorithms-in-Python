# problem link-->> https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        MAXV = 100000

        level = [0] * (MAXV + 1)
        height = [0] * (MAXV + 1)
        level_max = [0] * (MAXV + 1)
        level_second_max = [0] * (MAXV + 1)
        def compute(node , lev):
            if not node:
                return 0
            level[node.val] = lev

            height[node.val] =  max(compute(node.left , lev+1) ,compute(node.right , lev+1))+1

            if level_max[lev] < height[node.val]:
                level_second_max[lev] = level_max[lev]
                level_max[lev] = height[node.val]
            elif level_second_max[lev] < height[node.val]:
                level_second_max[lev] = height[node.val]
            
            return height[node.val]
        
        compute(root , 0)
        ans = []
        for node in queries:
            l = level[node]
            temp = l + (level_second_max[l] if level_max[l] == height[node] else level_max[l]) - 1
            ans.append(temp)
        return ans



        

            
        
