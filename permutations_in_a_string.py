from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # len_s1 = len(s1)
        # s1_counter = Counter(s1)
        # for i in range(len(s2) - len(s1) + 1):
        #     temp = Counter(s2[i:i+len_s1])
        #     if temp == s1_counter:
        #         return True
        # return False
        ### Upper took ~1500ms , I think I can do better
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        target = [0] * 26
        for x in A:
            target[x] += 1
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False
    # this has runtime 72ms, this one's fine