import os
import sys

dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)
from utils.generate_sql_to_create_DB_table import (
    generate_sql_to_create_db_table, generate_sql_to_delete_db_table
    )

# to be replaced with the actual column mapping

IS_HISTRORY_TABLE = True

table_name = "garbage_truck"

#行政區,里別,分隊,局編,車號,路線,車次,抵達時間,離開時間,地點,經度,緯度
col_map = {
    'district': 'character varying(50) COLLATE pg_catalog."default"',
    'village': 'character varying(50) COLLATE pg_catalog."default"',
    'team': 'character varying(50) COLLATE pg_catalog."default"',
    'station': 'character varying(50) COLLATE pg_catalog."default"',
    'car_number': 'character varying(50) COLLATE pg_catalog."default"',
    'route': 'character varying(50) COLLATE pg_catalog."default"',
    'arrival_time': 'timestamp without time zone',
    'departure_time': 'timestamp without time zone',
    'location': 'text COLLATE pg_catalog."default"',
    'lng': 'double precision',
    'lat': 'double precision'
}

if IS_HISTRORY_TABLE:
    table_name = [table_name, f"{table_name}_history"]

gen_sql = ""
for table in table_name:
    drop_table_sql = generate_sql_to_delete_db_table(table)
    create_table_sql = generate_sql_to_create_db_table(table, col_map)
    gen_sql += drop_table_sql + create_table_sql

save_path = os.path.join(dags_path, 'proj_city_dashboard', 'garbage_truck', 'sql_generate.sql')
with open(save_path, 'w') as f:
    f.write(gen_sql)