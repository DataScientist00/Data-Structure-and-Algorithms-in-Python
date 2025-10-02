# problem link-->> https://leetcode.com/problems/find-if-array-can-be-sorted/description/


# -----------O(n) solution -----------------------
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = float('-inf')
        cur_min = nums[0]
        cur_max = nums[0]
        for i in range(len(nums)-1):
            if bin(nums[i]).count('1') == bin(nums[i+1]).count('1'):
                cur_min = min(cur_min , nums[i+1])
                cur_max = max(cur_max , nums[i+1])
            else:
                if cur_min < prev_max:
                    return False
                else:
                    prev_max = cur_max
                    cur_min = nums[i+1]
                    cur_max = nums[i+1]
        if cur_min < prev_max:
            return False
        return True

# ---------- O(n^2) bubble sort solution--------------

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(len(nums)):
            swapped = False
            for j in range(n-i-1):
                if nums[j] < nums[j+1]:
                    continue
                else:
                    if bin(nums[j]).count('1') == bin(nums[j+1]).count('1'):
                        nums[j] , nums[j+1] = nums[j+1] , nums[j]
                        swapped = True
                    else:
                        return False
            if not swapped:
                break
        return True
        
