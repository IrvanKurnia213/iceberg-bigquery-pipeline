import pandas as pd
from sqlalchemy import create_engine

# 1. Connect to Trino
engine = create_engine("trino://admin@localhost:8080/iceberg/staging")

def export_table_to_parquet(table_name, output_file):
    print(f"Reading {table_name} from Trino/Iceberg...")
    
    # Query the data
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    
    # Export to Parquet
    print(f"Exporting to {output_file}...")
    df.to_parquet(output_file, index=False, engine='pyarrow')
    print(f"Successfully exported {len(df)} rows.")

# 2. Execute Exports
export_table_to_parquet("articles_metadata", "parquet/articles_metadata_gold.parquet")
export_table_to_parquet("clicks_sample", "parquet/clicks_sample_gold.parquet")

print("\n Parquet files for manual upload ready.")