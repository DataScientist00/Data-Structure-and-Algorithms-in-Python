# problem link-->> https://leetcode.com/problems/reordered-power-of-2/description/



class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def sort_it(n):
            return "".join(sorted(str(n)))

        target = sort_it(n)
        for i in range(31):
            if target == sort_it((1 << i)):
                return True
        return False
        
