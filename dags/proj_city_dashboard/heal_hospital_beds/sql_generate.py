import os
import sys

dags_path = os.path.join(os.getcwd(), 'dags')  # Should be looks like '.../dags'
sys.path.append(dags_path)
from utils.generate_sql_to_create_DB_table import (
    generate_sql_to_create_db_table, generate_sql_to_delete_db_table
    )

# to be replaced with the actual column mapping

IS_HISTRORY_TABLE = True

table_name = "heal_hospital_beds"

# 機構名稱	地址	電話	急性一般病床數	急性精神病床數	慢性一般病床數	慢性精神病床數	安寧病床數	加護病床（ICU）	急性呼吸照護病床	慢性呼吸照護病床	燒傷病床	急診觀察床	其他觀察病床	手術恢復床	嬰兒床	嬰兒病床	血液透析病床	腹膜透析病床	精神科加護病床	燒傷加護病床	普通隔離病床	正壓隔離病床	負壓隔離病床	骨髓移植病床
col_map = {
    #先加入data_time
    #data_time timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    "data_time": "timestamp with time zone DEFAULT CURRENT_TIMESTAMP",
    'name': 'character varying(50) COLLATE pg_catalog."default"',
    'district': 'character varying(50) COLLATE pg_catalog."default"',
    'addr': 'character varying(50) COLLATE pg_catalog."default"',
    'phone': 'character varying(50) COLLATE pg_catalog."default"',
    'acute_general_beds': 'integer',
    'acute_psychiatric_beds': 'integer',
    'chronic_general_beds': 'integer',
    'chronic_psychiatric_beds': 'integer',
    'palliative_beds': 'integer',
    'icu_beds': 'integer',
    'acute_respiratory_care_beds': 'integer',
    'chronic_respiratory_care_beds': 'integer',
    'burn_beds': 'integer',
    'emergency_observation_beds': 'integer',
    'other_observation_beds': 'integer',
    'surgical_recovery_beds': 'integer',
    'baby_beds': 'integer',
    'baby_sick_beds': 'integer',
    'hemodialysis_beds': 'integer',
    'peritoneal_dialysis_beds': 'integer',
    'psychiatric_icu_beds': 'integer',
    'burn_icu_beds': 'integer',
    'general_isolation_beds': 'integer',
    'positive_pressure_isolation_beds': 'integer',
    'negative_pressure_isolation_beds': 'integer',
    'bone_marrow_transplant_beds': 'integer',
    'lng': 'double precision',
    'lat': 'double precision',
    'wkb_geometry': 'geometry(Point,4326)'
}

if IS_HISTRORY_TABLE:
    table_name = [table_name, f"{table_name}_history"]

gen_sql = ""
for table in table_name:
    drop_table_sql = generate_sql_to_delete_db_table(table)
    create_table_sql = generate_sql_to_create_db_table(table, col_map)
    gen_sql += drop_table_sql + create_table_sql

save_path = os.path.join(dags_path, 'proj_city_dashboard', 'heal_hospital_beds', 'sql_generate.sql')
with open(save_path, 'w') as f:
    f.write(gen_sql)