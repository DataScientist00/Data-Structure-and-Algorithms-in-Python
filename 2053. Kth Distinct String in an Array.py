#problem link -->> https://leetcode.com/problems/kth-distinct-string-in-an-array/description/


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = defaultdict(int)
        c=1
        for i in arr:
            count[i] += 1
        for i in arr:
            if count[i] == 1:
                if c == k:
                    return i
                c += 1
        return ""
        
