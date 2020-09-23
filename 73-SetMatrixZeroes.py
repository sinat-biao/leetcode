"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 方法一：复制数组遍历，原数组上修改
        # 扫描所有位置，遇到 0，就将其所在行与列全部置零，但是这种方法会对被置零的位置让其行列也置零。
        # 所以可以复制一个数组，在该数组中搜索 0，然后在原数组中置零。
        # m = len(matrix)
        # n = len(matrix[0])
        # matrix_copy = [[0]*n for p in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         matrix_copy[i][j] = matrix[i][j]
        # for i in range(m):
        #     for j in range(n):
        #         if matrix_copy[i][j] == 0:
        #             # 行置零
        #             for k in range(n):
        #                 matrix[i][k] = 0
        #             # 列置零
        #             for k in range(m):
        #                 matrix[k][j] = 0
        # return matrix
    
        # 方法二：方法一改进
        # 方法一直接复制了整个数组，这是没有必要的，其实只需要记录下原数组中 0 的位置，之后再将这些 0 所在的行列全置零即可。
        # 此时只需要使用一个数组记录下 0 的位置即可。
        # m = len(matrix)
        # n = len(matrix[0])
        # zero_points = []
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             zero_points.append((i, j))
        # for point in zero_points:
        #     for i in range(m):
        #         matrix[i][point[1]] = 0
        #     for j in range(n):
        #         matrix[point[0]][j] = 0
        # return matrix
    
        # 方法三：方法二改进
        # 数组中元素范围限制在 -2^31 <= matrix[i][j] <= 2^31 - 1 之间，而在 python 中可以取到超出这个int类型之外的取值。
        # 所以可以将所有 0 所在的行、列置一个范围外的数，然后再将这些数置零。
        out_num = pow(2, 31)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = out_num
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = out_num
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == out_num:
                    matrix[i][j] = 0
        return matrix
        
        
S = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(S.setZeroes(matrix))
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(S.setZeroes(matrix))
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(S.setZeroes(matrix))