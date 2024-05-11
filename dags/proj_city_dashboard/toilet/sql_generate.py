import os
import sys

dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)
from utils.generate_sql_to_create_DB_table import (
    generate_sql_to_create_db_table, generate_sql_to_delete_db_table
    )

# to be replaced with the actual column mapping

IS_HISTRORY_TABLE = True

table_name = "toilet"

col_map = {
    #data_time timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    "data_time": "timestamp with time zone DEFAULT CURRENT_TIMESTAMP",
    "district": 'character varying(50) COLLATE pg_catalog."default"',
    "toilet_type": 'character varying(50) COLLATE pg_catalog."default"',
    "toilet_name": 'character varying(255) COLLATE pg_catalog."default"',
    "toilet_address": 'text COLLATE pg_catalog."default"',
    "lng": "double precision",
    "lat": "double precision",
    "wkb_geometry": 'geometry(Point,4326)',
    "management_unit": 'character varying(255) COLLATE pg_catalog."default"',
    "seats": "integer",
    "excellent": "integer",
    "superior": "integer",
    "normal": "integer",
    "improved": "integer",
    "accessible_seats": "integer",
    "family_seats": "integer"
}

if IS_HISTRORY_TABLE:
    table_name = [table_name, f"{table_name}_history"]

gen_sql = ""
for table in table_name:
    drop_table_sql = generate_sql_to_delete_db_table(table)
    create_table_sql = generate_sql_to_create_db_table(table, col_map)
    gen_sql += drop_table_sql + create_table_sql

save_path = os.path.join(dags_path, 'proj_city_dashboard', 'toilet', 'sql_generate.sql')
with open(save_path, 'w') as f:
    f.write(gen_sql)
