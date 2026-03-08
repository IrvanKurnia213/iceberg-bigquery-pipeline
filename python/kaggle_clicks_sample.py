import pandas as pd
import kagglehub
from sqlalchemy import create_engine, text

# 1. Get the path
path = kagglehub.dataset_download("gspmoreira/news-portal-user-interactions-by-globocom")
engine = create_engine("trino://admin@localhost:8080/iceberg/staging")

# 2. Load Clicks Sample
df_clicks = pd.read_csv(f"{path}/clicks_sample.csv")

df_clicks = df_clicks.rename(columns={
    'session_start': 'session_start_ts',
    'click_deviceGroup': 'click_device_group'
})

# 3. Create Clicks Table (Partitioned by click_os for analytics)
create_clicks_sql = """
CREATE TABLE IF NOT EXISTS clicks_sample (
    user_id BIGINT,
    session_id BIGINT,
    session_start_ts BIGINT,
    session_size INT,
    click_article_id BIGINT,
    click_timestamp BIGINT,
    click_environment INT,
    click_device_group INT,
    click_os INT,
    click_country INT,
    click_region INT,
    click_referrer_type INT
) WITH (
    format = 'PARQUET',
    partitioning = ARRAY['click_os']
)
"""

with engine.connect() as conn:
    conn.execute(text(create_clicks_sql))
    conn.commit()

# 4. Insert Data in smaller bites
print("Ingesting Articles Metadata in chunks...")

df_clicks.to_sql(
    "clicks_sample", 
    engine, 
    if_exists="append", 
    index=False, 
    # method="multi",
    chunksize=1000
)

print("Done with Metadata!")