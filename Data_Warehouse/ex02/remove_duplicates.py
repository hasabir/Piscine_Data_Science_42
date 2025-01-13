import psycopg2
# import os

output = f"""SELECT event_time, event_type, product_id, price, user_id, user_session
FROM public.customers
WHERE product_id = 5809103 
  AND event_type = 'remove_from_cart' 
  AND event_time = '2022-10-01 00:00:30+00'::timestamp with time zone;
"""


delet_request = f"""
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
    """


def print_rows(query, cursor):
    cursor.execute(query)
    print("The number of parts: ", cursor.rowcount)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def main():
    connection = psycopg2.connect(
        host='localhost',
        port='5432',
        database="piscineds",
        user='hasabir',
        password='mysecretpassword'

    )
    cursor = connection.cursor()

    print_rows(output, cursor)
    connection.commit()
    
    cursor.execute(delet_request)
    connection.commit()
    
    
    print_rows(output, cursor)
    connection.commit()

    
    
    # cursor.execute(output)
    # print("The number of parts: ", cursor.rowcount)
    # row = cursor.fetchone()

    # print(row)
    # while row is not None:
    #     print(row)
    #     row = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()



if __name__ == "__main__":
    main()