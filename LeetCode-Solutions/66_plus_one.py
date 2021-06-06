class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits)-1
        if digits[j] == 9:
            i = j
            carry = 1
            while i >=0 and digits[i] == 9:
                digits[i] = 0
                i = i - 1
                
            if i < 0:
                digits[0] += carry
                digits.append(0)
            else:
                digits[i] += carry
                
        else:
            digits[j] += 1
            
        return digits