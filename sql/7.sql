-- v1
select Laptop.model, price
from Laptop left join Product on Laptop.model=Product.model
where maker='B'
union
select PC.model, price
from PC left join Product on PC.model=Product.model
where maker='B'
union
select Printer.model, price
from Printer left join Product on Printer.model=Product.model
where maker='B'

-- v2











