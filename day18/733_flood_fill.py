# runtime: O(m x n)
# space: O(m x n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ori_val = image[sr][sc]
        if ori_val == color:
            return image

        rows = len(image)
        cols = len(image[0])

        image[sr][sc] = color
        if sr-1 >= 0 and image[sr-1][sc] == ori_val:
            self.floodFill(image, sr-1, sc, color)
        if sr+1 < rows and image[sr+1][sc] == ori_val:
            self.floodFill(image, sr+1, sc, color)
        if sc-1 >= 0 and image[sr][sc-1] == ori_val:
            self.floodFill(image, sr, sc-1, color)
        if sc+1 < cols and image[sr][sc+1] == ori_val:
            self.floodFill(image, sr, sc+1, color)

        return image
