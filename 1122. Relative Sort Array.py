#problem link--->>> https://leetcode.com/problems/relative-sort-array/description/


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        res = []
        res2 = []
        index = 0
        for i in arr2:
            for j in range(cnt[i]):
                res.append(i)
        for i in range(len(arr1)):
            if arr1[i] not in res:
                res2.append(arr1[i])
        res2.sort()
        res.extend(res2)
        return res

            

        
