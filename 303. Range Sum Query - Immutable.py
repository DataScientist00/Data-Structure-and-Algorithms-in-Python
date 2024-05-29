#Problem link --->>> https://leetcode.com/problems/range-sum-query-immutable/description/


class NumArray:

    def __init__(self, nums: List[int]):
        self.temp = []
        cur=0
        for n in nums:
            cur += n
            self.temp.append(cur)

        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.temp[right]
        return self.temp[right] - self.temp[left-1]
        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
