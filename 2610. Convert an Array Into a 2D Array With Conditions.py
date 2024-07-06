#problem link-->> https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        result = []
        for n in nums:
            temp=count[n]
            if len(result) == temp:
                result.append([])
            result[temp].append(n)
            count[n] += 1
        return result
