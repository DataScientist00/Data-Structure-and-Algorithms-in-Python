#problem link-->> https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        result = []
        for can in candies:
            if can + extraCandies >= maxx:
                result.append(True)
            else:
                result.append(False)
        return result
        
