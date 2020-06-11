class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        imageWidth = len(image)
        imageHeight = len(image[0])
        if oldColor == newColor:
            return image
        ##### Helper FXN ####################
        #####################################
        def flood_fill_inner(x, y):
            if image[x][y] == oldColor:
                image[x][y] = newColor
                if x > 0:
                    flood_fill_inner(x-1, y)
                if y > 0:
                    flood_fill_inner(x, y-1)
                if x < imageWidth-1: 
                    flood_fill_inner(x+1, y)
                if y < imageHeight-1:
                    flood_fill_inner(x, y+1)
        #####################################
        #####################################   
        flood_fill_inner(sr,sc)
        return image
