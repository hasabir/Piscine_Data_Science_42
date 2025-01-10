import psycopg2
import os
import pandas as pd
from sqlalchemy import create_engine



#dialect+driver://username:password@host:port/database

def main():
    engine = create_engine("postgresql+psycopg2://hasabir:mysecretpassword@localhost:5432/piscineds")
    connection = psycopg2.connect(
        host='localhost',
        port='5432',
        database="piscineds",
        user='hasabir',
        password='mysecretpassword'
    )
    
    cursor = connection.cursor()
    customer = pd.DataFrame()
    directory_path = "../subject"
    for root, _, files in os.walk(directory_path):
        current_dir = root.split('/')[-1:][0]
        for file in files:
            if current_dir == 'customer':
                customer = pd.concat([customer, pd.read_csv(f"{root}/{file}")])
    customer.to_sql('customer', connection, if_exists= 'replace')
    sql='''select * from customer;'''
    print(sql)
    cursor.execute(sql)
    cursor.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()