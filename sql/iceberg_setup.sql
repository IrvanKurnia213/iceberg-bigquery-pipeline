CREATE TABLE IF NOT EXISTS metastore.public.iceberg_tables (
  catalog_name varchar(255) NOT NULL,
  table_namespace varchar(255) NOT NULL,
  table_name varchar(255) NOT NULL,
  metadata_location varchar(255) DEFAULT NULL,
  previous_metadata_location varchar(255) DEFAULT NULL,
  PRIMARY KEY (catalog_name, table_namespace, table_name)
);

CREATE TABLE IF NOT EXISTS metastore.public.iceberg_namespaces (
  catalog_name varchar(255) NOT NULL,
  namespace varchar(255) NOT NULL,
  PRIMARY KEY (catalog_name, namespace)
);

CREATE TABLE IF NOT EXISTS metastore.public.iceberg_namespace_properties (
  catalog_name varchar(255) NOT NULL,
  namespace varchar(255) NOT NULL,
  property_key varchar(255) NOT NULL,
  property_value varchar(255) DEFAULT NULL,
  PRIMARY KEY (catalog_name, namespace, property_key)
);