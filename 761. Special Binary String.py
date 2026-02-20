# problem link -- >> https://leetcode.com/problems/special-binary-string/description/

class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        def solve(t):
            start = 0
            total  = 0
            ans = []
            for i in range(len(t)):
                total += 1 if t[i] == '1' else -1
                if total == 0:
                    temp = solve(t[start+1:i])
                    ans.append('1' + solve(temp) + '0')
                    start = i + 1

            ans.sort(reverse=True)
            return ''.join(ans)

        return solve(s)
        
