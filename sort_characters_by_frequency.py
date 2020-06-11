class Solution:
    def frequencySort(self, s: str) -> str:
        word_2_freq = {}
        for i in s:
            if i not in word_2_freq:
                word_2_freq[i] = 1
            else:
                word_2_freq[i] += 1
        sorted_w2f = sorted(word_2_freq.items(), key=lambda x:x[1], reverse=True)
        result = []
        for item in sorted_w2f:
            for _ in range(item[1]):
                result.append(item[0])
        return ''.join(result)