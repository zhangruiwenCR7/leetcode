#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#
# https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
#
# algorithms
# Easy (77.79%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 13.3K
# Testcase Example:  '[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]'
#
# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
# 
# 请你统计并返回 grid 中 负数 的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# 输出：8
# 解释：矩阵中共有 8 个负数。
# 
# 
# 示例 2：
# 
# 输入：grid = [[3,2],[1,0]]
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：grid = [[1,-1],[-1,-1]]
# 输出：3
# 
# 
# 示例 4：
# 
# 输入：grid = [[-1]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    # def countNegatives(self, grid: List[List[int]]) -> int:
    def countNegatives(self, grid) -> int:
        '''
        n = len(grid[0])
        res = 0
        end = n-1
        for i in range(len(grid)):
            b,e = 0,end
            while True:
                mid = (b+e+1)//2
                if grid[i][mid]<0:
                    e = mid
                else:
                    b = mid
                if b+1==e or b==e:
                    if grid[i][b]<0:
                        res += n-b
                    elif grid[i][e]>=0:
                        pass
                    else:
                        res += n-e
                    end = e
                    break
        return res
        '''
        res = 0
        n = len(grid[0])
        end = n-1
        for i in range(len(grid)):
            while grid[i][end]<0 and end>=0:
                end -= 1
            res += n-end-1
        return res

                
s=Solution()
case1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
case2 = [[3,2],[1,0]]
print(s.countNegatives(case1))      
# @lc code=end

