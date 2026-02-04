# Architecture

## Data Flow

Local:
- MinIO simulates AWS S3
- Apache Iceberg manages table metadata and data files
- Spark reads Iceberg tables using snapshot isolation

Cloud:
- Spark writes Parquet files to GCS
- BigQuery loads Parquet files for analytics

## Why Iceberg
- ACID transactions on object storage
- Schema evolution
- Snapshot-based incremental processing

## Why Spark
- Native Iceberg integration
- Efficient batch processing
- Reliable BigQuery ingestion

## What Is Simulated
- AWS S3 → MinIO

## What Is Real
- Google Cloud Storage
- BigQuery
