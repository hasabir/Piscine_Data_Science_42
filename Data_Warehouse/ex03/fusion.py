import psycopg2
import os
import pandas as pd
import sqlalchemy as sql


type_dict = {
    'product_id': sql.types.Integer,
    'category_id': sql.types.BIGINT,
    'category_code': sql.types.TEXT,
    'brand': sql.types.TEXT
}


join_query = f"""is this correct :
SELECT
    *
FROM
    customers
RIGHT JOIN item
    ON data_2022_dec.product_id = item.product_id;"""



def main():
    db = sql.create_engine("postgresql://hasabir:mysecretpassword@localhost:5432/piscineds")
    engine = db.connect()
    
    directory_path = "../subject"
    for root, _, files in os.walk(directory_path):
        current_dir = root.split('/')[-1]
        if current_dir == 'item':
            for file in files:
                print(file)
                customers  = pd.read_csv(f"{root}/{file}")
                customers.to_sql('customers', engine, if_exists='append', index=False, dtype=type_dict)
    
    engine.close()