"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modif
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 方法一：两次翻转
        # 顺时针旋转 90 度，可以发现等同于先将数组按对角线（左上-右下）翻转，再左右翻转
        # n = len(matrix)
        # # 对角线翻转
        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         if i < j:
        #             tmp = matrix[i][j]
        #             matrix[i][j] = matrix[j][i]
        #             matrix[j][i] = tmp
        # # print(matrix)
        # # 左右翻转
        # for row in range(n):
        #     for col in range(int(n/2)):
        #         tmp = matrix[row][col]
        #         matrix[row][col] = matrix[row][n-col-1]
        #         matrix[row][n-col-1] = tmp
        # # print(matrix)    
        
        # 方法二：依次旋转边角
        # 对边角元素进行4个元素一组的顺时针旋转操作（具体可参见官方题解）
        n = len(matrix)
        for i in range(int((n+1)/2)):
            for j in range(int(n/2)):
                tmp = []
                row = i
                col = j
                # 这一步比较巧妙，通过递推更新行列值来实现 4 个方向上的数据交换
                for k in range(4):
                    tmp.append(matrix[row][col])
                    x = row
                    row = col
                    col = n - 1 - x
                for k in range(4):
                    matrix[row][col] = tmp[(k+3)%4]
                    x = row
                    row = col
                    col = n - 1 - x
        print(matrix)
        
                         
S = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(S.rotate(matrix))
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(S.rotate(matrix))