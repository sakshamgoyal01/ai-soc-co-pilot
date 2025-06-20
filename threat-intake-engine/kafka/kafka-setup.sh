#!/bin/bash

# Wait for Kafka to be ready
echo "Waiting for Kafka to start..."
sleep 15

# Create 'threat-logs' topic manually (optional if auto-create is enabled)
docker-compose exec kafka \
  kafka-topics --create \
  --topic threat-logs \
  --partitions 1 \
  --replication-factor 1 \
  --if-not-exists \
  --bootstrap-server kafka:9092

echo "Kafka topic 'threat-logs' is ready."
