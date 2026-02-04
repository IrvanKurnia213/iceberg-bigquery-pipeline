# Iceberg -> BigQuery Pipeline

This project demonstrates a local-to-cloud data pipeline using:

- MinIO (S3-compatible storage)
- Apache Iceberg (table format)
- Apache Spark (batch processing)
- Google Cloud Storage (staging)
- BigQuery (analytics tool)

## Overview

In here Iceberg is used as a System of Record on Object Storage.
Spark reads snapshot-consistent data from Iceberg tables and
loads curated datasets into BigQuery via Parquet files on GCS.

This repository simulates AWS S3 locally using MinIO while
using real GCS and BigQuery for ingestion validation.