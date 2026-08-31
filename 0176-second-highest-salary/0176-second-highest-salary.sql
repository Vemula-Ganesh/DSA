# Write your MySQL query statement below
select max(salary) SecondHighestSalary from(select *,dense_rank() over(order by salary desc) rnk from employee) employee where rnk=2;