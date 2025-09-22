import os
from sqlalchemy import create_engine

from utils import (extract_data,
                   transform_data,
                   load_to_dw)


postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_port = str(os.getenv('POSTGRES_PORT'))
postgres_host = str(os.getenv('POSTGRES_HOST'))
postgres_dw = os.getenv('POSTGRES_DB')
csv_url = os.getenv('CSV_URL')

dw_engine_con = create_engine(f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_dw}')

print("Start of ETL Pipeline")

def run_etl_pipeline(csv_url, dw_engine_con):
    print("Extraction Begin...")
    df_extract = extract_data(csv_url)
    print("Extraction End.")

    print("Transformation Begin...")
    df_transform = transform_data(df_extract)
    print("Transformation End.")

    print("Loading to Data Warehouse Begin...")
    load_to_dw(df_transform, dw_engine_con)
    print("Loading to Data Warehouse End.")

print("Start of ETL Pipeline")

if __name__ == '__main__':
    run_etl_pipeline(csv_url, dw_engine_con)
