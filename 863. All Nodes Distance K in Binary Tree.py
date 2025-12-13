# problem link-->> https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}
        res = []

        def parent(node , par=None):
            if not node:
                return None
            if par:
                parent_map[node] = par
            
            parent(node.left , node)
            parent(node.right , node)

        parent(root)


        visited = set()
        def dfs(node , dist):
            if not node or node in visited:
                return 
            visited.add(node)
            if dist == k:
                res.append(node.val)
                return
            dfs(node.left , dist+1)
            dfs(node.right ,dist+1)
            dfs(parent_map.get(node) , dist+1)
        dfs(target , 0)
        return res

        
