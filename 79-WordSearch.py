"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution(object):
    def regsearch(self, board, aready_used, word, now_point, k):
        if k >= len(word):
            print('------------------')
            return True
        x = now_point[0]
        y = now_point[1]
        m = len(board)
        n = len(board[0])
        if x > 0:
            # print('>>>>>>>')
            if aready_used[x-1][y] == 0 and board[x-1][y] == word[k]:
                aready_used[x-1][y] = 1
                print([x-1, y], word[k], k)
                ret = self.regsearch(board, aready_used, word, [x-1, y], k+1)
                aready_used[x-1][y] = 0
                if ret:
                    return True
        if y > 0:
            if aready_used[x][y-1] == 0 and board[x][y-1] == word[k]:
                aready_used[x][y-1] = 1
                print([x, y-1], word[k], k)
                ret = self.regsearch(board, aready_used, word, [x, y-1], k+1)
                aready_used[x][y-1] = 0
                if ret:
                    return True
        if x < m - 1:
            # print('<<<<<<<')
            if aready_used[x+1][y] == 0 and board[x+1][y] == word[k]:
                aready_used[x+1][y] = 1
                print([x+1, y], word[k],k)
                ret = self.regsearch(board, aready_used, word, [x+1, y], k+1)
                aready_used[x+1][y] = 0
                if ret:
                    return True
        if y < n - 1:
            if aready_used[x][y+1] == 0 and board[x][y+1] == word[k]:
                aready_used[x][y+1] = 1
                print([x, y+1], word[k], k)
                ret = self.regsearch(board, aready_used, word, [x, y+1], k+1)
                aready_used[x][y+1] = 0
                if ret:
                    return True
        

    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 方法一：递归遍历
        # 用一个数组记录已访问位置，用一个常量记录当前需要匹配的单词字母，每次依次访问当前位置的4个相邻位置。
        # 若相邻位置元素与下一个字母匹配，向该方向递归。直到 word 全部被匹配完，返回 True。
        m = len(board)
        n = len(board[0])
        # 先定位到初始位置
        start_points = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start_points.append([i, j])
        print(start_points)
        # 从初始位置开始递归搜索
        # 用一个数组记录已访问位置
        aready_used = [[0]* n for k in range(m)]
        # print(aready_used)
        for point in start_points:
            aready_used[point[0]][point[1]] = 1
            contain = self.regsearch(board, aready_used, word, point, 1)
            aready_used = [[0]* n for k in range(m)]
            if contain:
                return True
        return False


S = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
print(S.exist(board, word))     # True
word = "SEE"
print(S.exist(board, word))     # True
word = "ABCB"
print(S.exist(board, word))     # False
board = [
  ['a','a'],
]
word = "aaa"
print(S.exist(board, word))     # False
board = [
  ['a','b'],
]
word = "ba"
print(S.exist(board, word))     # True
board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCESEEEFS"
print(S.exist(board, word))     # True
        