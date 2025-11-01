# problem link-->> https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        cumvalue = 0
        cumvaluesum = 0
        ans = [0] * len(boxes)
        for i in range(len(boxes)):
            ans[i] = cumvaluesum
            cumvalue += int(boxes[i])
            cumvaluesum += cumvalue

        cumvalue = 0
        cumvaluesum = 0
        for i in reversed(range(len(boxes))):
            ans[i] += cumvaluesum
            cumvalue += int(boxes[i])
            cumvaluesum += cumvalue
        return ans
