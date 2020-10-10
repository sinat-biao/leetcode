"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""
class Solution(object):
    def sumofarr(self, subarr, m, n, board_copy):
        # 计算位置元素
        sum_ = 0
        for i in subarr:
            if i[0] >= 0 and i[0] < m and i[1] >= 0 and i[1] < n:
                sum_ += board_copy[i[0]][i[1]]
        return sum_
        
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 方法一：复制数组更新
        m = len(board)
        n = len(board[0])
        board_copy = [[0]*n for i in range(m)]
        # print(board_copy)
        for i in range(m):
            for j in range(n):
                board_copy[i][j] = board[i][j]
        # print(board_copy)
        # update the board
        for i in range(m):
            for j in range(n):
                eight_neibo = []
                eight_neibo.append([i-1,j-1])
                eight_neibo.append([i-1,j])
                eight_neibo.append([i-1,j+1])
                eight_neibo.append([i, j-1])
                eight_neibo.append([i,j+1])
                eight_neibo.append([i+1,j-1])
                eight_neibo.append([i+1,j])
                eight_neibo.append([i+1,j+1])
                print(eight_neibo)
                sums = self.sumofarr(eight_neibo, m, n, board_copy)
                if sums < 2 and board[i][j] == 1:
                    board[i][j] = 0
                if (sums == 2 or sums == 3) and board[i][j] == 1:
                    pass
                if sums > 3 and board[i][j] == 1:
                    board[i][j] = 0
                if sums == 3 and board[i][j] == 0:
                    board[i][j] = 1
        return board


S = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(S.gameOfLife(board))