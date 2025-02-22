#problem link-->> https://leetcode.com/problems/largest-number/description/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator: sorts based on which concatenation is greater
        def compare(x, y):
            return -1 if x + y > y + x else 1
        
        # Convert integers to strings for concatenation and sorting
        nums = list(map(str, nums))
        
        # Sort using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join sorted numbers and handle case where leading number is '0'
        result = ''.join(nums)
        
        return '0' if result[0] == '0' else result
        
