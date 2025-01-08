CREATE TABLE public.data_2022_oct
(
    event_time timestamp with time zone,
    event_type character varying,
    product_id bigint,
    price numeric,
    user_id bigint,
    user_session uuid
);

ALTER TABLE IF EXISTS public.data_2022_oct
    OWNER TO hasabir;


\COPY public.data_2022_oct FROM '/tmp/data/customer/data_2022_oct.csv' DELIMITER ',' CSV HEADER;




-- #!/bin/bash

-- docker exec -i postgres_container psql -U hasabir -d piscineds -f /path/to/commands.sql


-- SELECT * FROM data_2022_oct;