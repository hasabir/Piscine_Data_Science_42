import psycopg2

output_query = """
SELECT event_time, event_type, product_id, price, user_id, user_session
FROM public.customers
WHERE product_id = 5809103 
  AND event_type = 'remove_from_cart' 
  AND event_time = '2022-10-01 00:00:30+00'::timestamp with time zone;
"""


def print_rows(query, cursor):
    """Execute a query and print the resulting rows."""
    cursor.execute(query)
    print("Number of rows retrieved:", cursor.rowcount)
    for row in cursor.fetchall():
        print(row)
    print('*'* 50)

def main():
    try:
        connection = psycopg2.connect(
            host='localhost',
            port='5432',
            database="piscineds",
            user='hasabir',
            password='mysecretpassword'
        )

        with open('remove_duplicates.sql', 'r') as file:
            delete_request = file.read()
        cursor = connection.cursor()

        print("Before Deletion:")
        print_rows(output_query, cursor)

        cursor.execute(delete_request)

        print("After Deletion:")
        print_rows(output_query, cursor)

        connection.commit()
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    main()