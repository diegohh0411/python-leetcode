# Created by Diego Hernández Herrera at 2026/11/01 19:48
# leetgo: 1.4.18
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import *
from leetgo_py import *
from collections import defaultdict

# @lc code=begin

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        map = defaultdict(int) # Keys are chars, and Values are the indices of the last time we saw this char

        i = -1

        for j in range(len(s)):
            # print("...")
            # print(f"Loop no. {j}, at char {s[j]}")
            if s[j] in map and map[s[j]] > i: # if we have seen this char before and it's within the current window
                # print(f"{s[j]} exists within the current window {i}:{j}")
                i = map[s[j]];
                # print(f"i was set to {i} so as to adjust the window, which is now {i}:{j}")

            current_len = j - i
            # print(f"Current length of window is: {current_len}")

            answer = max(answer, current_len)

            map[s[j]] = j
            j += 1

            # print(f"Answer is now: {answer}")

        return answer

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
