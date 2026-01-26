# problem link-->> https://leetcode.com/problems/minimum-absolute-difference/description/




class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        check = float('inf')
        for i in range(1,len(arr)):
            check = min(check , arr[i]-arr[i-1])
        ans = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == check:
                ans.append([arr[i-1],arr[i]])
        return ans
        
