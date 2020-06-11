# def number_of_ones(num):
#     ones = 1
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         while num > 1:
#             rem = num % 2
#             if rem == 1:
#                 ones += 1
#             num = num // 2
#         return ones

# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         output = []
#         for i in range(0, num+1):
#             output.append(number_of_ones(i))
#         return output
# * Accepted ~ 230 ms
# * TODO :et's try to improve it
class Solution:
    def countBits(self, num: int):
        res, i = [0,1], 1
        while i<num:
            i += len(res)
            res += [1+e for e in res]
            print(res)
        return res[:num+1]
# *  Acepted ~ 80ms

# ? Testing Code in Editor
s  = Solution()
s.countBits(5)