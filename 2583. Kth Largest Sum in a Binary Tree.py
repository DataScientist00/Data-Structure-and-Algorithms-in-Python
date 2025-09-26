# problem link-->> https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []
        def bfs(node):
            queue = deque([node])
            while queue:
                levelsum = 0
                for q in range(len(queue)):
                    node = queue.popleft()
                    levelsum += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                heapq.heappush(self.heap , -levelsum)
            
        bfs(root)
        if k > len(self.heap):
            return -1
        while k:
            val = heapq.heappop(self.heap)
            k -= 1
        return -1 * val
        
