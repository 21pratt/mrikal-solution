from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='End-to-end data pipeline',
    schedule_interval=timedelta(days=1),
)

start = DummyOperator(task_id='start', dag=dag)

ingest_network_logs = PythonOperator(
    task_id='ingest_network_logs',
    python_callable=stream_logs_to_kafka,
    dag=dag,
)

ingest_transactions = BashOperator(
    task_id='ingest_transactions',
    bash_command='bash /path/to/your/sqoop_job.sh',
    dag=dag,
)

transform_data = SparkSubmitOperator(
    task_id='transform_data',
    application='/path/to/your/spark_transformation_script.py',
    dag=dag,
)

load_data_to_redshift = PythonOperator(
    task_id='load_data_to_redshift',
    python_callable=load_data_to_redshift,
    dag=dag,
)

end = DummyOperator(task_id='end', dag=dag)

start >> [ingest_network_logs, ingest_transactions] >> transform_data >> load_data_to_redshift >> end
