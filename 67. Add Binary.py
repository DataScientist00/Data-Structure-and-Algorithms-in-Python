# problem link -- >> https://leetcode.com/problems/add-binary/description/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            result.append(str(total % 2))
            carry = 1 if total > 1 else 0
        
        return "".join(result[::-1])
