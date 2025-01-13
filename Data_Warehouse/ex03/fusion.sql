ALTER TABLE customers
ADD COLUMN category_id BIGINT,
ADD COLUMN category_code character varying,
ADD COLUMN brand character varying;


UPDATE customers
SET
    category_id = item.category_id,
    category_code = item.category_code,
    brand = item.brand
FROM item
WHERE customers.product_id = item.product_id;