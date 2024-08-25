#problem link-->> https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd Cycle Detection Algorithm
        temp1 = temp2 = 0
        while True: #In this loop check you check cycle exist or not
            temp1 = nums[temp1]
            temp2 = nums[nums[temp2]]
            if temp1 == temp2:
                break
        temp1 = 0
        #In this you find the starting node of the cycle
        while True:
            temp1 = nums[temp1]
            temp2 = nums[temp2]
            if temp1 == temp2:
                break
        return temp1



        
