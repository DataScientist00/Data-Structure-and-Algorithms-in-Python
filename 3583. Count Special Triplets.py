# problem link-->> https://leetcode.com/problems/count-special-triplets/description/



class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        MOD = 10 ** 9 + 7

        freqPrev = {}
        leftside = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                freqPrev[nums[0]] = 1
                continue
            if nums[i]*2 in freqPrev:
                leftside[i] = freqPrev[nums[i]*2]
            if nums[i] in freqPrev:
                freqPrev[nums[i]] += 1
            else:
                freqPrev[nums[i]] = 1

        freqNext = {}
        ans = 0
        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                freqNext[nums[i]] = 1
                continue
            if nums[i]*2 in freqNext:
                ans += leftside[i] * freqNext[nums[i]*2]
            if nums[i] in freqNext:
                freqNext[nums[i]] += 1
            else:
                freqNext[nums[i]] = 1

        return ans % MOD

        
