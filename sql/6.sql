select distinct maker, speed
from Laptop left join Product on Laptop.model=Product.model
where hd=10 or hd>10
