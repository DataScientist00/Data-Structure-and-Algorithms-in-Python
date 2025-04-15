# problem link-->> https://leetcode.com/problems/ones-and-zeroes/description/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)
        for s in strs:
            mcnt , ncnt = s.count('0') , s.count('1')
            for p in range(m , mcnt -1 , -1):
                for q in range(n , ncnt -1 , -1):
                    dp[(p , q)] =  max(1 + dp[(p - mcnt , q - ncnt )] , dp[(p , q)])
        return dp[(m , n)]
        
