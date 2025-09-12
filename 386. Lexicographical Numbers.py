# problem link-->> https://leetcode.com/problems/lexicographical-numbers/description/


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(num):
            if num > n:
                return
            ans.append(num)
            num *= 10
            for i in range(10):
                dfs(num + i)

        for i in range(1,10):
            dfs(i)
        return ans
            
        
