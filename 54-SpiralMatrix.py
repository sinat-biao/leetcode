"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 方法一：顺序取值
        # 
        # m = len(matrix)
        # if m == 0:
        #     return []
        # n = len(matrix[0])
        # al = m * n
        # list_ = []
        # row = [i for i in range(m)]
        # col = [i for i in range(n)]
        # while True:
        #     print(row, col)
            
        #     row_ = row[0]
        #     for j in col:
        #         list_.append(matrix[row_][j])
        #         print(list_)
            
        #     row.pop(0)
        #     if len(row) == 0:
        #         return list_
            
        #     col_ = col[-1]
        #     for i in row:
        #         list_.append(matrix[i][col_])
        #         print(list_)
            
        #     col.pop(-1)
        #     if len(col) == 0:
        #         return list_
            
        #     col_rev = [k for k in col]
        #     col_rev.reverse()
        #     row_ = row[-1]
        #     for j in col_rev:
        #         list_.append(matrix[row_][j])
        #         print(list_)
        #     row.pop(-1)
            
        #     row_rev = [k for k in row]
        #     row_rev.reverse()
        #     col_ = col[0]
        #     for i in row_rev:
        #         list_.append(matrix[i][col_])
        #         print(list_)
        #     col.pop(0)
            
        #     if len(list_) == al:
        #         return list_
            
        # 方法二：方法一改进
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        al = m * n
        list_ = []
        row = [i for i in range(m)]
        col = [i for i in range(n)]
        while True:
            print(row, col)
            
            row_ = row[0]
            for j in col:
                list_.append(matrix[row_][j])
                print(list_)
            
            row.pop(0)
            if len(row) == 0:
                return list_
            
            col_ = col[-1]
            for i in row:
                list_.append(matrix[i][col_])
                print(list_)
            
            col.pop(-1)
            if len(col) == 0:
                return list_
            
            row_ = row[-1]
            j_v = len(col) - 1
            while j_v >= 0:
                list_.append(matrix[row_][col[j_v]])
                j_v -= 1
                print(list_)
            row.pop(-1)
            
            col_ = col[0]
            i_v = len(row) - 1
            while i_v >= 0:
                list_.append(matrix[row[i_v]][col_])
                i_v -= 1
                print(list_)
            col.pop(0)
            
            if len(list_) == al:
                return list_
            
            
S = Solution()
matrix = [[ 1, 2, 3 ], 
          [ 4, 5, 6 ], 
          [ 7, 8, 9 ]]
print(S.spiralOrder(matrix))
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]]
print(S.spiralOrder(matrix))
matrix = []
print(S.spiralOrder(matrix))