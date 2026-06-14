# Product Price at a Given Date
# Difficulty: Medium
# Date: 2026-06-14
# LeetCode: https://leetcode.com/problems/product-price-at-a-given-date/
# Status: Accepted
# Runtime: 696 ms
# Memory: 0B
SELECT product_id,
    IFNULL(
        (SELECT new_price FROM Products
         WHERE product_id = p.product_id AND change_date <= '2019-08-16'
         ORDER BY change_date DESC LIMIT 1),
        10
    ) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
