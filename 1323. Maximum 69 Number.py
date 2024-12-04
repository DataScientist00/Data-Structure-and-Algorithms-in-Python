#problem link-->> https://leetcode.com/problems/maximum-69-number/description/


class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        max_num_str = num_str.replace('6', '9', 1)
        return int(max_num_str)

        
