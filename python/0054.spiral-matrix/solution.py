# Created by Diego Hernández Herrera at 2026/11/02 09:15
# leetgo: 1.4.18
# https://leetcode.com/problems/spiral-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = n
        t = 0
        b = m

        answer = []

        while l < r or t < b:
            for j in range(l, r):
                answer.append(matrix[t][j])
            t += 1
            for i in range(t, b):
                answer.append(matrix[i][r - 1])
            r -= 1
            for j in reversed(range(l, r)):
                answer.append(matrix[b - 1][j])
            b -= 1
            for i in reversed(range(t, b)):
                answer.append(matrix[i][l])
            l += 1

        return answer


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().spiralOrder(matrix)
    print("\noutput:", serialize(ans, "integer[]"))
