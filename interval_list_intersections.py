class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # A = [[0,2],[5,10],[13,23],[24,25]]
        # B = [[1,5],[8,12],[15,24],[25,26]]
        # OP = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        i = 0
        j = 0
        na = len(A)
        nb = len(B)
        result = []
        while i < na and j < nb:
            lowerBound = max(A[i][0], B[j][0])
            upperBound = min(A[i][1], B[j][1])
            if lowerBound <= upperBound:
                result.append([lowerBound, upperBound])
            if upperBound == A[i][1]:
                i += 1
            else:
                j += 1
        return result
        # Runtime ~  160ms