# problem link-->> https://leetcode.com/problems/count-elements-with-maximum-frequency/description


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = defaultdict(dict)
        maxx = float('-inf')
        for n in nums:
            
            count[n] = count.get(n,0) + 1
            maxx = max(maxx , count[n])
        
        ans = 0
        for i , j in count.items():
            if j == maxx:
                ans += maxx
        return ans
