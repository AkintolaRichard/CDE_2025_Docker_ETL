import pandas as pd

def extract_data(csv_url):
    df = pd.read_csv(csv_url)
    return df

def transform_data(df):
    df.columns = [ (col.replace(" ", "_")).lower() for col in df.columns]
    return df

def load_to_dw(df, dw_engine_con):
    df.to_sql(name='worldgdps', con=dw_engine_con, if_exists='replace', schema='public', index=False)

