select Ships.class, name, country
from Ships left join Classes on Ships.class=Classes.class
where numGuns>=10
