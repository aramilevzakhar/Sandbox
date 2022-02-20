select t1.model, t2.model, t1.speed, t1.ram, t2.speed, t2.ram
from 
(select *
from PC) as t1,
(select *
from PC) as t2
group by ram;


-- right
select max(t1.model), min(t2.model), t1.speed, t1.ram
from 
(select *
from PC) as t1,
(select *
from PC) as t2
where t1.ram=t2.ram and t1.speed=t2.speed and t1.model!=t2.model
group by t1.model, t2.model, t1.speed, t1.ram
having max(t1.model) > min(t2.model);
