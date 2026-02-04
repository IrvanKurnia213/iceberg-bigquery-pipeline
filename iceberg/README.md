# Apache Iceberg

Iceberg tables act as the system of record.
They are stored on object storage and managed
via a catalog (Hive Metastore).

Data in BigQuery is always derived from Iceberg
snapshots and is never written directly.
