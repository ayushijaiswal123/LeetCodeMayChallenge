class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        '''
        slope1 = y1 - y0 / x1 - x0
        slope2 = y2 - y1 / x2 - x1
        comparing two:
            slope1 = slope2
            (y1 - y0 / x1 - x0) = (y2 - y1 / x2 - x1)
            shifting denominators
            (y1 - y0)*(x2 -x1) = (y2 - y1)*(x1 - x0)
        '''
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            if  (y1 - y0)*(xi - x1) != (yi - y1)*(x1 - x0):
                return False
        return True
