sqoop import --connect jdbc:mysql://your-rds-endpoint/database_name \
  --username your_username --password your_password \
  --table transactions --target-dir s3a://your-staging-bucket/transactions/ \
  --incremental append --check-column id --last-value 0
