import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load transformed data
transformed_data = spark.read.parquet("s3a://your-staging-bucket/transformed-data/")

# Write to Redshift
transformed_data.write \
    .format("com.databricks.spark.redshift") \
    .option("url", "jdbc:redshift://your-redshift-cluster:5439/yourdb?user=youruser&password=yourpassword") \
    .option("dbtable", "transaction_facts") \
    .option("tempdir", "s3a://your-temp-bucket/temp-dir/") \
    .mode("overwrite") \
    .save()

job.commit()
