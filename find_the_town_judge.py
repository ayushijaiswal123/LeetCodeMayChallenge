class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        person_he_trusts_dict = {i:0 for i in range(1, N+1)}
        person_trusts_him = {i:0 for i in range(1, N+1)}
        for pair in trust:
            person_he_trusts_dict[pair[0]] += 1
            person_trusts_him[pair[1]] += 1
        for i in range(1,N+1):
            if person_he_trusts_dict[i] == 0 and person_trusts_him[i] == N-1:
                return i
        return -1
