import psycopg2
import os
import pandas as pd
import sqlalchemy as sql

type_dict = {
    'event_time': sql.types.TIMESTAMP(timezone=True),
    'event_type': sql.types.TEXT,
    'product_id': sql.types.BIGINT,
    'price': sql.types.NUMERIC,
    'user_id': sql.types.BIGINT,
    'user_session': sql.types.UUID
}

def create_table():
    return f"""
CREATE TABLE IF NOT EXISTS public.customer (
    event_time TIMESTAMP WITH TIME ZONE,
    event_type character varying,
    product_id bigint,
    price numeric,
    user_id bigint,
    user_session uuid
);"""

def main():
    engine = sql.create_engine("postgresql+psycopg2://hasabir:mysecretpassword@localhost:5432/piscineds")
    connection = psycopg2.connect(
        host='localhost',
        port='5432',
        database="piscineds",
        user='hasabir',
        password='mysecretpassword'
    )

    
    
    cursor = connection.cursor()
    cursor.execute(create_table()) 
    customer = pd.DataFrame()
    directory_path = "../subject"
    for root, _, files in os.walk(directory_path):
        current_dir = root.split('/')[-1]
        for file in files:
            if current_dir == 'customer':
                print(f"{root}/{file}")
                customer = pd.concat([customer, pd.read_csv(f"{root}/{file}")])

    customer.to_sql('customer', engine, if_exists='replace', index=False, dtype=type_dict)
    query = 'SELECT * FROM customer;'
    cursor.execute(query)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
