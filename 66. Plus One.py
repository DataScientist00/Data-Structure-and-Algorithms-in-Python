


# problem link -- >https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur = ''.join(str(item) for item in digits)
        temp = int(cur) + 1
        x = str(temp)
        result = []
        for i in x:
            result.append(int(i))
        return result
        
