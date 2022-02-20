select model, speed, hd 
from PC 
where price < 600 and (cd = '24x' or cd='12x')
