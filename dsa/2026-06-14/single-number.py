# Single Number
# Difficulty: Easy
# Date: 2026-06-14
# LeetCode: https://leetcode.com/problems/single-number/
# Status: Accepted
# Runtime: 4 ms
# Memory: 21.1 MB

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result
