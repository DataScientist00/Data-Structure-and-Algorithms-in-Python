
# problem link-->> https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        j = len(arr)-1
        n = len(arr)
        while j > 0 and arr[j-1] <= arr[j]:
            j -= 1

        ans = j
        i = 0 
        while i < j and (i == 0 or arr[i] >= arr[i-1]):
            while j < n and arr[i] > arr[j]:
                j += 1

            ans = min(ans , j-i-1)
            i += 1

        return ans
        
