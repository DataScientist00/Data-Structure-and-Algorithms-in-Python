# problem link-->> https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = 0
        res = []
        n = len(nums)
        for i in range(n-k+1):
            count = Counter(nums[i:i+k])
            if len(count) <= x:
                res.append(sum(nums[i:i+k]))
            else:
                temp = list(count.items())
                temp.sort(key = lambda p:(p[1],p[0]),reverse = True)
                cur_sum = 0
                for i , n in temp[:x]:
                    cur_sum += (i*n)
                res.append(cur_sum)
        return res
                

        
