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
CREATE TABLE public.test (
    product_id bigint,
    category_id bigint,
    category_code character varying,
    brand character varying
);

ALTER TABLE IF EXISTS public.test OWNER TO hasabir;

COPY public.test FROM '/tmp/data/item/item.csv' DELIMITER ',' CSV HEADER;

SELECT * FROM test;
"""

cursor.execute(sql)
connection.commit()

cursor.close()
connection.close()
