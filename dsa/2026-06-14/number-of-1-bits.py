# Number of 1 Bits
# Difficulty: Easy
# Date: 2026-06-14
# LeetCode: https://leetcode.com/problems/number-of-1-bits/
# Status: Accepted
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
