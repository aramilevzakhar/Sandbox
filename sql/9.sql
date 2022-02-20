SELECT distinct maker
FROM PC left join Product on PC.model=Product.model
WHERE speed>=450
