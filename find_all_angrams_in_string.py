from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not p or len(p) > len(s):
            return []
        len_p = len(p)
        len_s = len(s)
        p = list(p)
        p.sort()
        seen = set()
        indices = []
        for i in range(len_s-len_p+1):
            anagram = s[i:i+len_p]
            if anagram in seen:
                indices.append(i)
                continue
            str_anagram = anagram
            anagram = sorted(list(anagram))
            if anagram == p:
                indices.append(i)
                seen.add(str_anagram)
        return indices