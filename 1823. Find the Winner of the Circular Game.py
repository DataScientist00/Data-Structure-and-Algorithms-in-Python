# problem link-->> https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()
        for i in range(1,n+1):
            q.append(i)
        while len(q) > 1:
            for i in range(k-1):
                a = q.popleft()
                q.append(a)
            q.popleft()
        return q[0]
        
