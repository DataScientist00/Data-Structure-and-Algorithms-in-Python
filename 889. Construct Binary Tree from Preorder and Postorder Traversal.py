# problem link-->> https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos_to_idx = {}
        for i , n in enumerate(postorder):
            pos_to_idx[n] = i

        def build(i1,i2,j1,j2):
            if i1 > i2 or j1 > j2:
                return None
            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_val = preorder[i1+1]
                mid = pos_to_idx[left_val]
                size = mid - j1 + 1
                root.left = build(i1+1 , i1+size ,j1 , mid)
                root.right = build(i1+size+1 , i2 , mid+1 ,j2-1)
            return root

        return build(0,len(preorder)-1 , 0 , len(postorder)-1)

        
        
