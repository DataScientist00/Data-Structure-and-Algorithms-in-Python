# Question Link --> https://leetcode.com/problems/add-to-array-form-of-integer/description/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        size = 0
        num.reverse()
        while k:
            digit = k % 10
            if size < len(num):
                num[size] += digit
            else:
                num.append(digit)
            
            carry = num[size] // 10
            num[size] = num[size] % 10

            k = k // 10
            k += carry
            size += 1
        num.reverse()
        return num


       
        

    
        
        


        
        
