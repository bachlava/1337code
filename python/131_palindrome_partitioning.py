"""
Given a string s, partition s such that every substring of the partition
is a palindrome. Return all possible palindrome partitioning of s.
Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.
"""
from typing import List
import collections


class Solution:
    def __init__(self):
        self.memory = collections.defaultdict(list)

    # Credits to linfq
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        if s in self.memory:
            return self.memory[s]
        result = []
        for i in range(1, len(s) + 1):
            prefix = s[: i]
            if self.is_palindrome(prefix):
                for suffix in self.partition(s[i :]):
                    result.append([prefix] + suffix)
        self.memory[s] = result
        return result

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]


if __name__ == '__main__':
    s1 = "aab"
    print(Solution().partition(s1))
    s2 = "a"
    print(Solution().partition(s2))
