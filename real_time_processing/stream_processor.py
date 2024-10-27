
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('your_topic', bootstrap_servers='localhost:9092')

for message in consumer:
    data = json.loads(message.value.decode('utf-8'))
    print(f"Processed message: {data}")
