#problem link-->>> https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res , temp = [] , []

        def dfs(i):
            if i == len(s):
                res.append(temp[:])
                return

            for j in range(i , len(s)):
                if self.check_palindrome(i , j , s):
                    temp.append(s[i:j+1])
                    dfs(j+1)
                    temp.pop()

        dfs(0)
        return res

    def check_palindrome(self , l , r , s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
