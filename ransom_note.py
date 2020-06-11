from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = Counter(magazine)
        print(magazine_dict)
        for char in ransomNote:
            if char in magazine_dict:
                if magazine_dict[char] > 0:
                    magazine_dict[char] -= 1
                else:
                    return False
            else:
                return False
        return True
