from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

spark = SparkSession.builder \
    .appName("DataTransformation") \
    .getOrCreate()

# Load data
network_logs_df = spark.read.json("s3a://your-staging-bucket/network-logs/")
transactions_df = spark.read.parquet("s3a://your-staging-bucket/transactions/")

# Data Cleaning
network_logs_df = network_logs_df.dropna().dropDuplicates()
transactions_df = transactions_df.dropna().dropDuplicates()

# Standardize formats
transactions_df = transactions_df.withColumn("timestamp", col("timestamp").cast("timestamp"))

# Data Integration
integrated_df = network_logs_df.join(transactions_df, "user_id")

# Perform necessary calculations/aggregations
integrated_df = integrated_df.groupBy("user_id").agg(
    {"page_views": "sum", "transaction_amount": "sum"}
).withColumnRenamed("sum(page_views)", "total_page_views") \
 .withColumnRenamed("sum(transaction_amount)", "total_transaction_amount")

# Save the transformed data
integrated_df.write.parquet("s3a://your-staging-bucket/transformed-data/")
