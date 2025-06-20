import time, json, os
from confluent_kafka import Producer, KafkaException

KAFKA_BROKER = 'kafka:9092'
TOPIC = 'threat-logs'

# Configure the Kafka producer
producer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'queue.buffering.max.messages': 100000,
    'default.topic.config': {'acks': 'all'}
}

producer = Producer(producer_conf)
log_path = "/logs/simulated.log"
os.makedirs("/logs", exist_ok=True)

def delivery_report(err, msg):
    if err is not None:
        print(f"[❌] Message delivery failed: {err}")
    else:
        print(f"[✅] Message delivered to {msg.topic()} [{msg.partition()}]")
    print(f"🚀 Sending logs to Kafka broker at {KAFKA_BROKER}")
while True:
    try:
        # Simulate log data
        log = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "service": "firewall",
            "severity": "warning",
            "message": "Blocked suspicious IP"
        }
        with open(log_path, "a") as f:
            f.write(json.dumps(log) + "\n")
        print(f"[✅] Wrote log to {log_path}")
        # Convert to JSON and send to Kafka
        producer.produce(TOPIC, value=json.dumps(log), callback=delivery_report)
        producer.poll(0)  # Trigger delivery report callbacks

    except KafkaException as e:
        print(f"[⚠️] KafkaException occurred: {e}")
        time.sleep(5)

    except BufferError as e:
        print(f"[⚠️] Local buffer full, backing off: {e}")
        producer.poll(1)

    except Exception as e:
        print(f"[‼️] Unexpected error: {e}")
        time.sleep(5)

    time.sleep(3)

