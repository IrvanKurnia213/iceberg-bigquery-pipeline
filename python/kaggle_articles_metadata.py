import pandas as pd
import kagglehub
from sqlalchemy import create_engine, text

# 1. Get the path
path = kagglehub.dataset_download("gspmoreira/news-portal-user-interactions-by-globocom")
engine = create_engine("trino://admin@localhost:8080/iceberg/staging")

# 2. Load Metadata
df_meta = pd.read_csv(f"{path}/articles_metadata.csv")

# 3. Create Table (Partitioned by category for performance)
create_meta_sql = """
CREATE TABLE IF NOT EXISTS articles_metadata (
    article_id BIGINT,
    category_id BIGINT,
    created_at_ts BIGINT,
    publisher_id BIGINT,
    words_count INT
) WITH (
    format = 'PARQUET',
    partitioning = ARRAY['category_id']
)
"""

with engine.connect() as conn:
    conn.execute(text(create_meta_sql))
    conn.commit()

# 4. Insert Data in smaller bites
print("Ingesting Articles Metadata in chunks...")

df_meta.to_sql(
    "articles_metadata", 
    engine, 
    if_exists="append", 
    index=False, 
    method="multi",
    chunksize=5000
)

print("Done with Metadata!")