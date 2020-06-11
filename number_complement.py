class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        return num ^ (2**num.bit_length()-1)
            
