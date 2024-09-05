#problem link-->>> https://leetcode.com/problems/combinations/description/


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res , temp = [] , []
        num = [i+1 for i in range(n)]
        def backtrack(i):
            if len(temp) == k:
                res.append(temp[:])
                return
            if i >= len(num):
                return
            temp.append(num[i])
            backtrack(i+1)
            temp.pop()
            backtrack(i+1) 
              
        backtrack(0)        
        return res






        
