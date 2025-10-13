# problem link-->>> https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        arr = defaultdict(int)
        for i,w in enumerate(words):
            arr[i] = Counter(w)
        res = []
        res.append(words[0])
        for i in range(1,len(words)):
            if arr[i-1] != arr[i]:
                res.append(words[i])
        return res
        
        
