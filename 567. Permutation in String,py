#problem link-->> https://leetcode.com/problems/permutation-in-string/description/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s11 = Counter(s1)
        def check(s):
            s12 = Counter(s)
            counter = 0
            for i in range(len(s)):
                    if s11[s[i]] == s12[s[i]]:
                        counter += 1
            if counter == len(s):
                return True
        l = 0
        for r in range(len(s1),len(s2)+1):
            res = check(s2[l:r])
            if res == True:
                return True
            l += 1
        return False


        
