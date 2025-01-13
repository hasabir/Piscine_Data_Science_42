import os
import pandas as pd
import sqlalchemy as sql


type_dict = {
    'event_time': sql.types.TIMESTAMP(timezone=True),
    'event_type': sql.types.TEXT,
    'product_id': sql.types.INTEGER,
    'price': sql.types.NUMERIC,
    'user_id': sql.types.BIGINT,
    'user_session': sql.types.UUID
}

def main():
    db = sql.create_engine("postgresql://hasabir:mysecretpassword@localhost:5432/piscineds")
    engine = db.connect()
    
    directory_path = "../subject"
    for root, _, files in os.walk(directory_path):
        current_dir = root.split('/')[-1]
        if current_dir == 'customer':
            for file in files:
                print(file)
                customers  = pd.read_csv(f"{root}/{file}")
                customers.to_sql('customers', engine, if_exists='append', index=False, dtype=type_dict)
    
    engine.close()

if __name__ == "__main__":
    main()
