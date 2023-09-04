# Write your MySQL query statement below
select * from Cinema where id%2!=0 and description not in (select description from Cinema where description='boring') order by rating desc;