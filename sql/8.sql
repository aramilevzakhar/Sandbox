-- v1
select maker
from PC left join Product on PC.model=Product.model
except
select maker
from Laptop left join Product on Laptop.model=Product.model

-- v2
select maker
from PC left join Product on PC.model=Product.model
where maker not in 
(select maker
from Laptop left join Product on Laptop.model=Product.model)
