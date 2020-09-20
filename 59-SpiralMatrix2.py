"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 方法一：螺旋遍历
        # 利用 row、col 两个数组来记录当前行、列的范围，然后在此范围内进行遍历
        # k = 1
        # matrix = [ [0] * n for i in range(n)]   # python 创建二维数组
        # print(matrix)
        # row = [i for i in range(n)]
        # col = [i for i in range(n)]
        # while len(row) != 0 and len(col) != 0:
        #     # 行（从左到右）
        #     for i in col:
        #         matrix[row[0]][i] = k
        #         k += 1
        #     if len(row) > 0:
        #         row.pop(0)
        #     # 列（从上到下）
        #     for j in row:
        #         matrix[j][col[-1]] = k
        #         k += 1
        #     if len(col) > 0:
        #         col.pop()
        #     # 行（从右到左）
        #     col_rev = [i for i in col]
        #     col_rev.reverse()
        #     for i in col_rev:
        #         matrix[row[-1]][i] = k
        #         k += 1
        #     if len(row) > 0:
        #         row.pop()
        #     # 列（从下到上）
        #     row_rev = [i for i in row]
        #     row_rev.reverse()
        #     for j in row_rev:
        #         matrix[j][col[0]] = k
        #         k += 1
        #     if len(col) > 0:
        #         col.pop(0)
        # return matrix
    
        # 方法二：方法一改进
        # 用 4 个指针分别维护行、列的左右、上下范围，并采用 while 遍历的方式，减小方式一中拷贝数组带来的空间开销
        k = 1
        matrix = [ [0] * n for i in range(n)]   # python 创建二维数组
        print(matrix)
        row_left = 0
        row_right = n - 1
        col_left = 0
        col_right = n - 1
        while row_left <= row_right and col_left <= col_right:
            # 行（从左到右）
            for i in range(col_left, col_right + 1):
                matrix[row_left][i] = k
                k += 1
            if row_left <= row_right:
                row_left += 1
            # 列（从上到下）
            for j in range(row_left, row_right + 1):
                matrix[j][col_right] = k
                k += 1
            if col_left <= col_right:
                col_right -= 1
            # 行（从右到左）
            for i in range(col_right, col_left - 1, -1):
                matrix[row_right][i] = k
                k += 1
            if row_left <= row_right:
                row_right -= 1
            # 列（从下到上）
            for j in range(row_right, row_left - 1, -1):
                matrix[j][col_left] = k
                k += 1
            if col_left <= col_right:
                col_left += 1
        return matrix


S = Solution()
n = 3
print(S.generateMatrix(n))