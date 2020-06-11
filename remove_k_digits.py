class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        num = list(num)
        while k > 0:
            k -= 1
            i = 0
            while i < len(num)-1:
                if num[i] > num[i+1]:
                    break
                i += 1
            num = num[:i] + num[i+1:]
        return str(int(''.join(num)))
