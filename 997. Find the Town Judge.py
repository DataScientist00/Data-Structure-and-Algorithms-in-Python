#problem link-->> https://leetcode.com/problems/find-the-town-judge/description/


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc = defaultdict(int)
        out = defaultdict(int)
        for num in trust:
            inc[num[0]] += 1
            out[num[1]] += 1
        for i in range(1,n+1):
            if out[i] == n-1 and inc[i]==0:
                return i
        return -1


        
