import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('olist_order_reviews_dataset.csv')

df['review_creation_date'] = pd.to_datetime(df['review_creation_date'], errors='coerce')
df['review_answer_timestamp'] = pd.to_datetime(df['review_answer_timestamp'], errors='coerce')

engine = create_engine('mysql+pymysql://root:freyabala@localhost/ecommerce')

df.to_sql('reviews', engine, if_exists='replace', index=False)

print("Done. Rows loaded:", len(df))