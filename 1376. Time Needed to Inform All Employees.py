# problem link -- >> https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

class Solution:
    def numOfMinutes(self, n: int, headid: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)

        res = 0
        q = deque([(headid , 0)])
        while q:
            i , time = q.popleft()
            res = max(res , time)
            for nei in adj[i]:
                q.append((nei , time + informTime[i]))
        return res
        
