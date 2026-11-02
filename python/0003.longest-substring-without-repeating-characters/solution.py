# Created by Diego Hernández Herrera at 2026/11/02 10:01
# leetgo: 1.4.18
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from signal import default_int_handler
from typing import *
from leetgo_py import *
from collections import defaultdict

# @lc code=begin

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer: int = 0
        indexes: defaultdict[str, int] = defaultdict(int)
        i: int = -1
        current_char: str = ""
        window_len: int = 0

        for j in range(len(s)):
            current_char = s[j]

            if current_char in indexes and indexes[current_char] > i:
                i = indexes[current_char]

            window_len = j - i


            answer = max(answer, window_len)

            indexes[current_char] = j
            j += 1

        return answer



# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
