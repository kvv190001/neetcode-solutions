SELECT name
FROM Employee
JOIN (
    SELECT managerId FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
) E2 ON Employee.id = E2.managerId
