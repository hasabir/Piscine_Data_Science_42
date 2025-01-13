import psycopg2


def main():
    try:
        connection = psycopg2.connect(host='localhost', port='5432', database="piscineds",
            user='hasabir',
            password='mysecretpassword'
        )
        cursor = connection.cursor()
        with open("fusion.sql", 'r') as file:
            fusion_query = file.read()
        cursor.execute(fusion_query)

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