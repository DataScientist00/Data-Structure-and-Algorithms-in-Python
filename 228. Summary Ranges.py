
# problem link-->> https://leetcode.com/problems/summary-ranges/description/?cong=true

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ans = []
        build = str(nums[0])
        temp = ''

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                temp = str(nums[i])
            else:
                if temp == '':
                    ans.append(build)
                else:
                    ans.append(build + '->' + temp)
                build = str(nums[i])
                temp = ''

        # add the last range
        if temp == '':
            ans.append(build)
        else:
            ans.append(build + '->' + temp)

        return ans
