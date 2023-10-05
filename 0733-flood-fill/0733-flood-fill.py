class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not image:
            return image

        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]

        if start_color == color:
            return image

        stack = [(sr, sc)]

        while stack:
            r, c = stack.pop()

            if 0 <= r < rows and 0 <= c < cols and image[r][c] == start_color:
                image[r][c] = color
                stack.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])

        return image