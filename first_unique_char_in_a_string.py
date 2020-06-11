class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
                
        unique_chars = []
        for key in count:
            if count[key] == 1:
                unique_chars.append(key)
                
        for i in range(len(s)):
            if s[i] in unique_chars:
                return i
        return -1
