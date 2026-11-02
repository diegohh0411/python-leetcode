# Created by Diego Hernández Herrera at 2026/11/01 19:16
# leetgo: 1.4.18
# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import *
from leetgo_py import *
from collections import defaultdict

# @lc code=begin

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix_sum = 0
        psfm = defaultdict(int) # PSFM stands for prefix sum frequency map
        psfm[0] = 1;

        for x in nums:
            prefix_sum += x;
            answer += psfm.get(prefix_sum - k, 0);
            psfm[prefix_sum] = psfm.get(prefix_sum, 0) + 1;

        return answer

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraySum(nums, k)
    print("\noutput:", serialize(ans, "integer"))
