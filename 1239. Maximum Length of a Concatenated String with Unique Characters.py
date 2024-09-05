#problem link-->> https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]
        
        def backtrack(i , temp):
            res[0] = max(res[0], len(temp))

            for j in range(i , len(arr)):
                if set(temp).intersection(arr[j]):
                    continue
                if len(set(arr[j])) != len(arr[j]):
                    continue

                backtrack(j+1 ,temp + arr[j] )
        backtrack(0 , '')
        return res[0]
        
        
