-- SELECT price FROM customers WHERE event_type = 'purchase';



-- SELECT price AS COUNT FROM customers WHERE event_type = 'purchase';

-- DROP FUNCTION get_price();

CREATE OR REPLACE FUNCTION get_price()
RETURNS TABLE(price NUMERIC) AS $$
BEGIN
    RETURN QUERY SELECT customers.price FROM customers WHERE event_type = 'purchase';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_customer_number()
RETURNS TABLE(count BIGINT) AS $$
BEGIN
	RETURN QUERY SELECT COUNT(*) FROM customers WHERE event_type = 'purchase';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_event_time()
RETURNS TABLE(event_time TIMESTAMP WITH TIME ZONE) AS $$
BEGIN
	RETURN QUERY SELECT customers.event_time FROM customers WHERE event_type = 'purchase';
END;
$$ LANGUAGE plpgsql;