# Created by Diego Hernández Herrera at 2026/11/02 09:15
# leetgo: 1.4.18
# https://leetcode.com/problems/group-anagrams/

from tokenize import group
from typing import *
from leetgo_py import *
from collections import defaultdict

# @lc code=begin

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer: list[list[str]] = []
        groupings: defaultdict[str, list[str]] = defaultdict(list)
        key: str = ""

        for item in strs:
            key = "".join(sorted(item))
            if key in groupings:
                groupings[key].append(item)
            else:
                groupings[key] = [ item ]

        for key, values in groupings.items():
            answer.append(values)

        return answer


# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)
    print("\noutput:", serialize(ans, "string[][]"))
