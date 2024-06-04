#problem link--->>> https://leetcode.com/problems/shuffle-the-array/description/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i]=nums[i] << 10

            nums[i]=nums[i] | nums[i+n]
            k=2*n-1
        for i in range(n-1,-1,-1):
                y=nums[i]&(2**10 - 1)
                x=nums[i] >> 10
                nums[k]=y
                nums[k-1]=x
                k-=2

        return nums



        
