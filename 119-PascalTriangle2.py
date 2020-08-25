'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 先构造出 k(从0开始) 行的杨辉三角，然后返回第 k 行
        # pascal_triangle = []
        # for i in range(rowIndex+1):
        #     pascal_item = []
        #     for j in range(i+1):
        #         if j == 0 or i == j:
        #             pascal_item.append(1)
        #         else:
        #             pascal_item.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
        #     pascal_triangle.append(pascal_item)
        # return pascal_triangle[rowIndex]
    
        # 不构造整个三角，只是记录两行数组
        # pre_row = []
        # for i in range(rowIndex + 1):
        #     row = []
        #     for j in range(i+1):
        #         if j == 0 or i == j:
        #             row.append(1)
        #         else:
        #             row.append(pre_row[j-1] + pre_row[j])
        #     pre_row = row
        # return row
        
        # 空间复杂度：O(k)
        # 利用一行，然后后面一行直接利用当前行的值进行计算，然后插入到后面一行的合适位置
        row = []
        for i in range(rowIndex + 1):
            if i < 2:
                row.append(1)
            else:
                # 只插入一个，其余都是覆盖
                # 先插入一个元素
                for j in range(i-1, 0, -1):
                    if j == i-1:    # 只在最后一个位置执行插入（原数组中是倒数第二个）
                        row.insert(j, row[j-1] + row[j])
                        continue
                    else:
                        row[j] = row[j-1] + row[j]
            # print(row)
        return row
    

S = Solution()
print(S.getRow(3))
            
        