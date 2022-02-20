https://sql-ex.ru/
select
  distinct maker
from
  Product
where
  type = 'Printer';
select
  model,
  speed,
  hd
from
  PC;
select
  *
from
  PC;
select
  maker,
  speed
from
  Laptop
  right join Product on Laptop.model = Product.model
where
  hd >= 10
order by
  speed asc;
select
  fi.model,
  fi.price
from
  (
    select
      model,
      price
    from
      PC
    union
    select
      model,
      price
    from
      Laptop
    union
    select
      model,
      price
    from
      Printer
  ) as fi
  left join Product on Product.model = fi.model
where
  Product.maker = 'B';

select
  maker
from
  Product
where
  type = 'PC'
except
select
  maker
from
  Product
where
  type = 'Laptop';

select
  distinct maker
from
  PC
  left join Product on PC.model = Product.model
where
  speed >= 450;


-- 10
select
  model,
  price
from
  Printer
where
  price = (
    select
      max(price)
    from
      Printer
  );

-- 11
select
  avg(speed)
from
  PC;

-- create table Printer(speed integer);
-- Find out the average speed of the laptops priced over $1000.  12;

--12
select 
	avg(speed)
from
	Laptop where price>1000;
--select
--  avg(speed)
--from
--  Printer;

--13;
select 
  avg(speed) 
from
  PC right join Product on PC.model=Product.model
where maker='A';

-- For the ships in the Ships table that have at least 10 guns, get the class, name, and country.
-- 14
select 
	Ships.class, name, country
from
	Ships left join Classes on Ships.class=Classes.class
where 
	guns>=10;

-- 15
select 
 hd, count(hd) as quantity
from 
 PC
group by hd;

select 
 hd
from 
 PC
group by hd
having count(hd)>1;


-- 16
select 
fi1.ram, fi1.speed, fi2.ram, fi2.speed
from
(select ram, speed
from PC) as fi1,
(select ram, speed
from PC) as fi2
where fi1.ram=fi2.ram and fi1.speed=fi2.speed


select t1.model, t2.model, t1.speed, t1.ram
from
(select *
from PC) as t1,
(select *
from PC) as t2
where t1.ram=t2.ram and t1.speed=t2.speed and t1.model!=t2.model;


-- 17
-- Get the laptop models that have a speed smaller than the speed of any PC.
-- Result set: type, model, speed.

-- wrong
select type, Laptop.model, speed
from Laptop left join Product on Laptop.model=Product.model
where speed<(select min(speed)
from PC);

select type, Laptop.model, speed
from Laptop left join Product on Laptop.model=Product.model
where not speed >= any (select speed
from PC);

-- Find the makers of the cheapest color printers.
-- Result set: maker, price.

select maker, price
from Printer right join Product on Printer.model=Product.model
where color='y' and price=(select min(price)
from Printer
where color='y');


select *
from Printer
where color='y';


select *
from Product left join Printer on Printer.model=Product.model
where Product.type='Printer';


-- This is left join
select *
from Product left join (select * from Printer where color='y') as fi on fi.model=Product.model
where Product.type='Printer';


select maker, price
from Printer left outer join Product on Printer.model=Product.model
where color='y' and price=(select min(price)
from Printer
where color='y');


-- 19
select maker, avg(screen)
from Laptop inner join Product on Laptop.model=Product.model
group by maker;



create table users(
name varchar(30),
age  integer(30),
sex boolean

)

do $$
	declare
		counter interer := 0;
	begin
		while counter < 10 loop
			insert into users (first_name) values ('sseee');
			counter := counter + 1;
		end loop;
end$$;














