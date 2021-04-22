-- write your code in PostgreSQL 9.4
select q1.country, q1.sumofimporter, q2.sumofexporter
from (
     select c.country
            ,COALESCE(sum(t.value), 0) as sumofimporter
     from companies c
     full outer join trades t on t.seller = c.name
     group by c.country
) q1
join (
    select c.country
           ,COALESCE(sum(t2.value), 0) as sumofexporter
    from companies c
    full outer join trades t2 on t2.buyer = c.name
    group by c.country
) q2 on q2.country = q1.country
order by q1.country