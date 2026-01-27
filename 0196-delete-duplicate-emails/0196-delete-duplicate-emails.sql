/* Write your PL/SQL query statement below */
Delete from Person where id not in (select min(id) from person group by email);