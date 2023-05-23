# Write your MySQL query statement below
SELECT t1.firstName, t1.lastName, t2.city,t2.state
FROM Person as t1
LEFT Join Address as t2 ON t1.personID = t2.personID