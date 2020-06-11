class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result = []
        for i, pt in enumerate(points):
            result.append((i, pt[0]*pt[0] + pt[1]*pt[1]))
        result.sort(key=lambda x: x[1])
        result = result[:K]
        final = []
        for item in result:
            final.append(points[item[0]])
        return final