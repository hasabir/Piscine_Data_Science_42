import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="piscineds",
    user="hasabir",
    password="mysecretpassword"
)

cursor = connection.cursor()

sql = """
CREATE TABLE public.data_2022_oct (
    event_time TIMESTAMP WITH TIME ZONE,
    event_type character varying,
    product_id bigint,
    price numeric,
    user_id bigint,
    user_session uuid
);

ALTER TABLE IF EXISTS public.data_2022_oct OWNER TO hasabir;

COPY public.data_2022_oct FROM '/tmp/data/customer/data_2022_oct.csv' DELIMITER ',' CSV HEADER;

"""


cursor.execute(sql)
connection.commit()

cursor.close()
connection.close()
