import os
import sys

dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)
from utils.generate_sql_to_create_DB_table import (
    generate_sql_to_create_db_table, generate_sql_to_delete_db_table
    )

# to be replaced with the actual column mapping

IS_HISTRORY_TABLE = False
table_name = "di_park"

# seqno,pm_name,pm_longitude,pm_latitude,pm_unit,pm_location,di_hospital,di_fire,di_police,capacity
# name: type
col_map = {
    "seqno": "int",
    "pm_name": "text",
    "pm_longitude": "numeric",
    "pm_latitude": "numeric",
    "pm_unit": "text",
    "pm_location": "text",
    "di_hospital": "text",
    "di_fire": "text",
    "di_police": "text",
    "capacity": "int"
}

if IS_HISTRORY_TABLE:
    table_name = [table_name, f"{table_name}_history"]

gen_sql = ""

drop_table_sql = generate_sql_to_delete_db_table(table_name)
create_table_sql = generate_sql_to_create_db_table(table_name, col_map, is_add_mtime=False, is_add_ctime=False)
gen_sql += drop_table_sql + create_table_sql

save_path = os.path.join(dags_path, 'proj_city_dashboard', 'di_park', 'sql_generate.sql')
with open(save_path, 'w') as f:
    f.write(gen_sql)