# problem link-->> https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/



class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def getsum(count, x):
            # Sum of decreasing sequence: (x-1) + (x-2) + ... for `count` terms
            return count * x - (count * (count + 1)) // 2

        left, right = 1, maxSum
        result = 0

        while left <= right:
            mid = (left + right) // 2

            # ---- left side ----
            left_count = min(index, mid - 1)
            left_sum = getsum(left_count, mid)
            left_sum += index - left_count  # fill remaining with 1s

            # ---- right side ----
            right_count = min(n - index - 1, mid - 1)
            right_sum = getsum(right_count, mid)
            right_sum += (n - index - 1) - right_count  # fill remaining with 1s

            # ---- total ----
            total_sum = left_sum + mid + right_sum

            if total_sum <= maxSum:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
