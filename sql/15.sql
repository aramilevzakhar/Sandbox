-- without having
select hd
from (select count(hd) as count1, hd
from PC
group by hd) as fi
where fi.count1>=2


-- having
select hd
from PC
group by hd
having count(hd)>=2
