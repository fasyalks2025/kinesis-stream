import boto3
import json
import time
import random

stream_name = 'SensorDataStream' # NOTE: change according to your kinesis stream name
region_name = 'ap-southeast-1' # NOTE: change according to your region

kinesis_client = boto3.client('kinesis', region_name=region_name)

def generate_random_data():
    return {
        "sensor_id": random.randint(1, 10),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2),
        "event_time": time.time()
    }

def send_data_to_kinesis():
    while True:
        data = generate_random_data()
        partition_key = str(data['sensor_id'])
        print(f"Sending data: {data}")
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=partition_key
        )
        time.sleep(1)

if __name__ == "__main__":
    print("Streaming random sensor data to Kinesis...")
    send_data_to_kinesis()
