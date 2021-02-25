#
# @lc app=leetcode.cn id=73 lang=python
#
# [73] 矩阵置零
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        lst_row = []
        lst_col = []
        rows,cols = len(matrix),len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    lst_row.append(row)
                    lst_col.append(col)
        set_row = set(lst_row)
        set_col = set(lst_col)
        # print(,matrix[1][1])
        print(set_row)
        print(set_col)
        for i in set_row:
            matrix[i] = [0] * cols
        for j in set_col:
            for row in range(rows):
                # print(row)
                # print("matrix[1][1]",matrix[row][j])
                matrix[row][j] = 0
        return matrix

# if __name__ == '__main__':
#     solution = Solution()
#     print(solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
# @lc code=end

