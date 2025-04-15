SELECT event_time,
       user_id,
       price
FROM customers
WHERE event_type = 'purchase'
ORDER BY event_time;







-- SELECT price FROM customers WHERE event_type = 'purchase';



-- SELECT price AS COUNT FROM customers WHERE event_type = 'purchase';

-- DROP FUNCTION get_price();

-- CREATE OR REPLACE FUNCTION get_price()
-- RETURNS TABLE(event_time TIMESTAMP WITH TIME ZONE,
-- 				event_type character varying,
-- 				product_id bigint,
-- 				price numeric) AS $$
-- BEGIN
--     RETURN QUERY SELECT customers.price, customers.event_time, customers.event_type, customers.user_id  FROM customers;
-- END;
-- $$ LANGUAGE plpgsql;


-- CREATE OR REPLACE FUNCTION get_customer_number()
-- RETURNS TABLE(count BIGINT) AS $$
-- BEGIN
-- 	RETURN QUERY SELECT COUNT(*) FROM customers WHERE event_type = 'purchase';
-- END;
-- $$ LANGUAGE plpgsql;


-- CREATE OR REPLACE FUNCTION get_event_time()
-- RETURNS TABLE(event_time TIMESTAMP WITH TIME ZONE) AS $$
-- BEGIN
-- 	RETURN QUERY SELECT customers.event_time FROM customers WHERE event_type = 'purchase';
-- END;
-- $$ LANGUAGE plpgsql;