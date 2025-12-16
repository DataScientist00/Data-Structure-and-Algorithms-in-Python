# problem link-->> https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def find(node , target):
            if not node:
                return 
            if node.val == target:
                return node
            return find(node.left , target) or find(node.right,target)
        sta = find(root , start)


        pitaji = {}
        def parent(node , par):
            if not node:
                return None
            pitaji[node] = par
            parent(node.left , node)
            parent(node.right , node)

        parent(root , None)


        q = deque([sta])
        ans = 0
        visited = {sta}   # mark start visited immediately

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)

                if pitaji[node] and pitaji[node] not in visited:
                    visited.add(pitaji[node])
                    q.append(pitaji[node])

            ans += 1

        return ans - 1
