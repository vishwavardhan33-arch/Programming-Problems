class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        oldcolor = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        if oldcolor!=color:
            self.dfs(sr,sc,rows,cols,oldcolor,color,image)
        return image
    def dfs(self,sr,sc,rows,cols,oldcolor,newcolor,image):
        if sr<0 or sc<0 or sr>=rows or sc>=cols or image[sr][sc]!=oldcolor:
            return 
        image[sr][sc] = newcolor
        self.dfs(sr+1,sc,rows,cols,oldcolor,newcolor,image)
        self.dfs(sr-1,sc,rows,cols,oldcolor,newcolor,image)
        self.dfs(sr,sc+1,rows,cols,oldcolor,newcolor,image)
        self.dfs(sr,sc-1,rows,cols,oldcolor,newcolor,image)
