# problem link-->> http://leetcode.com/problems/sequential-digits/description/

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        for i in range(1, 10):
            num = i

            for j in range(i + 1, 10):
                num = num * 10 + j

                if low <= num <= high:
                    result.append(num)

        return sorted(result)
