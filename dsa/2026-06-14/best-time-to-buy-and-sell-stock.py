# Best Time to Buy and Sell Stock
# Difficulty: Easy
# Date: 2026-06-14
# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Status: Accepted
# Runtime: 52 ms
# Memory: 28.5 MB

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit
