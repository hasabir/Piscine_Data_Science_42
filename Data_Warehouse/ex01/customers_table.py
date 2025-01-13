import psycopg2
import os
import pandas as pd
import sqlalchemy as sql



def main():
    db = sql.create_engine("postgresql://hasabir:mysecretpassword@localhost:5432/piscineds")
    engine = db.connect()
    
    directory_path = "../subject"
    for root, _, files in os.walk(directory_path):
        current_dir = root.split('/')[-1]
        if current_dir == 'customer':
            for file in files:
                file_path = f"{root}/{file}"
                print(file_path)
                customers  = pd.read_csv(file_path)
                # for chunk in pd.read_csv(file_path, chunksize=10000):
                customers.to_sql('customers', engine, if_exists='append', index=False)
    
    engine.close()

if __name__ == "__main__":
    main()
