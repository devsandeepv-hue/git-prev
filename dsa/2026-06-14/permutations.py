# Permutations
# Difficulty: Medium
# Date: 2026-06-14
# LeetCode: https://leetcode.com/problems/permutations/
# Status: Accepted
# Runtime: 0 ms
# Memory: 19.5 MB
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def bt(path, remaining):
            if not remaining: res.append(path[:]); return
            for i in range(len(remaining)):
                path.append(remaining[i])
                bt(path, remaining[:i] + remaining[i+1:])
                path.pop()
        bt([], nums)
        return res
