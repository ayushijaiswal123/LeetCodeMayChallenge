class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while (i**2 <= num):
            if (num % i == 0) and (num / i == i):
                return True
            i+= 1
        return False
