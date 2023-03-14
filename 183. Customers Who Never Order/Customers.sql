# Write your MySQL query statement below
SELECT Customers.Name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM orders)
