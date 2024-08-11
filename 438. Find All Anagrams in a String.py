#problem link-->> https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        l = 0
        if len(p) > len(s):
            return []
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        for i in range(len(p)):
            count1[s[i]] += 1
            count2[p[i]] += 1
        if count1 == count2:
            res.append(0)
        for r in range(len(p) , len(s)):
            count1[s[r]] += 1
            count1[s[l]] -= 1
            if count1[s[l]] == 0:
                count1.pop(s[l])
            l += 1
            if count1 == count2:
                res.append(l)
        return res

        


        
