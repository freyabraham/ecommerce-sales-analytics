import pandas as pd
from sqlalchemy import create_engine
import datetime as dt

engine = create_engine('mysql+pymysql://root:freyabala@localhost/ecommerce')

query = """
SELECT o.order_id, o.customer_id, c.customer_unique_id, 
       o.order_purchase_timestamp, p.payment_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN payments p ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
"""

df = pd.read_sql(query, engine)
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Snapshot date = one day after the most recent order in the dataset
snapshot_date = df['order_purchase_timestamp'].max() + dt.timedelta(days=1)

# Group by customer_unique_id and calculate R, F, M
rfm = df.groupby('customer_unique_id').agg({
    'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days,  # Recency
    'order_id': 'nunique',                                                  # Frequency
    'payment_value': 'sum'                                                  # Monetary
}).reset_index()

rfm.columns = ['customer_unique_id', 'Recency', 'Frequency', 'Monetary']

print("Total customers:", len(rfm))
print(rfm.head(10))
print(rfm.describe())

# Segment customers: One-time vs Repeat buyers
rfm['customer_type'] = rfm['Frequency'].apply(lambda x: 'Repeat Buyer' if x > 1 else 'One-Time Buyer')

segment_summary = rfm.groupby('customer_type').agg(
    num_customers=('customer_unique_id', 'count'),
    avg_monetary=('Monetary', 'mean'),
    total_revenue=('Monetary', 'sum')
).reset_index()

segment_summary['pct_of_customers'] = round(100 * segment_summary['num_customers'] / len(rfm), 1)
segment_summary['pct_of_revenue'] = round(100 * segment_summary['total_revenue'] / rfm['Monetary'].sum(), 1)

print("\n--- Customer Segments ---")
print(segment_summary)

# Save to CSV so we can inspect it
rfm.to_csv('rfm_output.csv', index=False)
print("\nSaved to rfm_output.csv")