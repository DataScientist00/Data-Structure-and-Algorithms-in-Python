# problem link-->> https://leetcode.com/problems/minimum-index-of-a-valid-split/description/



class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = Counter(nums)

        for i in range(len(nums)):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            left_length = i + 1
            right_length = len(nums) - i - 1

            if left[nums[i]] > left_length //2 and right[nums[i]] > right_length // 2:
                return i
        return -1
