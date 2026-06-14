# Missing Number
# Difficulty: Easy
# Date: 2026-06-14
# LeetCode: https://leetcode.com/problems/missing-number/
# Status: Accepted
# Runtime: 0 ms
# Memory: 20.4 MB

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
