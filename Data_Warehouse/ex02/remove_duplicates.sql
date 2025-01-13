DELETE FROM customers
USING (
    SELECT ctid, product_id, user_id, event_type, user_session
    FROM (
        SELECT ctid, product_id, user_id, event_type, user_session,
               ROW_NUMBER() OVER (
                   PARTITION BY product_id, user_id, event_type, user_session
                   ORDER BY product_id ASC
               ) AS row_num
        FROM customers
    ) AS subquery
    WHERE row_num > 1
) AS duplicates
WHERE customers.ctid = duplicates.ctid;