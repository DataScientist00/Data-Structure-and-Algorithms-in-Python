#problem link--->> https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
         a, b = defaultdict(int) , defaultdict(int)

         for i , j in zip(target, arr):
            a[i] += 1
            b[j] += 1
         if len(a) != len(b):
            return False
         for i in a:
            if a[i] != b[i]:
                return False
         return True
        
