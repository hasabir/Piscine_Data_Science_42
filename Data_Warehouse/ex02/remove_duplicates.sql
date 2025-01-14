
WITH CTE AS (
    SELECT 
        ctid,
        ROW_NUMBER() OVER (
            PARTITION BY product_id, user_id, event_type, user_session
            ORDER BY product_id
        ) AS row_num
    FROM customers
)
DELETE FROM customers
WHERE ctid IN (
    SELECT ctid
    FROM CTE
    WHERE row_num > 1
);
