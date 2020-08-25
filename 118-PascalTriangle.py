"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 方法一：利用性质递推下一行的元素
        pascal_triange = []
        for i in range(numRows):
            pascal_item = []
            for j in range(i+1):
                if j == 0 or j == i:
                    pascal_item.append(1)
                else:
                    if i == 0:
                        continue
                    else:
                        pascal_item.append(pascal_triange[i-1][j-1] + pascal_triange[i-1][j])
            # print(pascal_item)
            pascal_triange.append(pascal_item)
        return pascal_triange
    
    
S = Solution()
print(S.generate(5))