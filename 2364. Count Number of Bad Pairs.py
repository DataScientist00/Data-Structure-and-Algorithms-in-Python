# problem link-->> https://leetcode.com/problems/count-number-of-bad-pairs/description/


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # convert the checking codition to nums[i] - i != nums[j] - j
        temp = []
        for i,n in enumerate(nums):
            temp.append(n-i)  # nums[i] - i != nums[j] - j
        leftside = {}
        ans = 0
        for i,n in enumerate(temp):
            if n in leftside:
               ans += (i-leftside[n])
               leftside[n] += 1
            else:
                leftside[n] = 1
                ans += i
        return ans 


        
