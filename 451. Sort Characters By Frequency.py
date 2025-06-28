# problem link-->> https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s) # chr -->> cnt
        freq = defaultdict(list)
        res = []
        for i , j in count.items():
            freq[j].append(i)
        for i in range(len(s) , 0,-1):
            for c in freq[i]:
                res.append(c * i)
        return "".join(res)

        
