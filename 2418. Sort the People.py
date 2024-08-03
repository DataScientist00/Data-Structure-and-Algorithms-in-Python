#problem link--->> https://leetcode.com/problems/sort-the-people/description/


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_name = {}
        for i , j in zip(names,heights):
            height_to_name[j] = i
        res = []
        for k in reversed(sorted(height_to_name)):
            res.append(height_to_name[k])
        return res
        

        
        
