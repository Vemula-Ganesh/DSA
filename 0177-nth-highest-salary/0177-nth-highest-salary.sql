CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select max(salary) from (select *,dense_rank() over(order by salary desc) rnk
from employee) employee where rnk=N
  );
END