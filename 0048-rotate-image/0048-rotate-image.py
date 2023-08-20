class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r=0,len(matrix)-1
        while l<r:
            for i in range(r-l):
                top,bot=l,r
                #save top left
                topleft=matrix[top][l+i]
                #move bottom left into top left
                matrix[top][l+i]=matrix[bot-i][l]
                #move bottom right into bottom left
                matrix[bot-i][l]=matrix[bot][r-i]
                #move top right into bottom right
                matrix[bot][r-i]=matrix[top+i][r]
                #move top left to top right
                matrix[top+i][r]=topleft
            r-=1
            l+=1