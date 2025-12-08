# problem link-->> https://leetcode.com/problems/count-square-sum-triples/description

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            for j in range(i+1 , n+1):
                c2 = i ** 2 + j ** 2
                temp = int(c2 ** 0.5)
                if temp <= n and temp * temp == c2:
                    ans += 2
        return ans
        
