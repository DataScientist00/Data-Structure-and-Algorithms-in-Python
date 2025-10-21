# problem link-->> https://leetcode.com/problems/adding-spaces-to-a-string/description/


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        ans = []
        for t in spaces:
            ans.append(s[j:t])
            j = t
        ans.append(s[j:])
        return ' '.join(ans)

        
