#problem link-->> https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""
        count1 , count2 = defaultdict(int) , defaultdict(int)
        for c in t:
            count1[c] +=1
        have , need = 0 , len(count1)
        res1,res2 , reslen = 0 , 0 , float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            count2[c] +=1
            if c in count1 and count2[c] == count1[c]:
                have +=1
            while have == need:
                if (r-l+1) < reslen:
                    res1 , res2 = l , r
                    reslen = (r-l+1)
                count2[s[l]] -= 1
                if s[l] in count1 and count2[s[l]] < count1[s[l]]:
                    have -=1
                l +=1
        return s[res1:res2 + 1] if reslen != float("inf") else ""
