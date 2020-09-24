"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 方法一：暴力搜索
        # m = len(matrix)
        # if m == 0:
        #     return False
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True
        # return False
    
        # 方法二：区间搜索
        # 先通过每一行的首末位值找到所在行，再在行内搜索
        # m = len(matrix)
        # if m == 0:
        #     return False
        # n = len(matrix[0])
        # if n == 0:
        #     return False
        # for i in range(m):
        #     if target >= matrix[i][0] and target <= matrix[i][n-1]:
        #         if matrix[i].__contains__(target):
        #             return True
        #         else:
        #             return False
        # return False         
    
        # 方法三：直接对整个数组实现二分查找
        # 整个二维数组有序，所以可以使用二分查找，与一维数组不同的是在二维中需要根据当前值转换出行、列值。
        # 考虑到此时数组的总长度为 $end=mxn$，中间位置为 $mid=(start+end)/2$，那么 mid 所在的行列可通过如下方式计算：
        # row = mid / n
        # col = mid % m
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        start = 0
        end = m * n - 1
        while start <= end:
            mid = int((start + end) / 2)
            row = int(mid / n)
            col = int(mid % n)
            print(start, end, mid, matrix[row][col])
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                start = mid + 1
            if matrix[row][col] > target:
                end = mid - 1
        return False
        
    
S = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print(S.searchMatrix(matrix, target))
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
print(S.searchMatrix(matrix, target))
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 10
print(S.searchMatrix(matrix, target))