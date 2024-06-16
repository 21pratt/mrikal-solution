from kafka import KafkaProducer
import json
import boto3
import time

s3 = boto3.client('s3')
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def stream_logs_to_kafka(bucket_name, prefix):
    result = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    for obj in result.get('Contents', []):
        response = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
        log_data = response['Body'].read().decode('utf-8')
        producer.send('network-logs', log_data)
        time.sleep(1)  # simulate streaming

if __name__ == "__main__":
    stream_logs_to_kafka('your-data-lake-bucket', 'network-logs/')
